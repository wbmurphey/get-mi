# get-mi
## Gets a specified mi number

## How to install:

Run the ```setup_get-mi.sh``` script from within this repo's folder.

## How to use:
Running ```get-mi argument1 argument2``` will return a single mi-number to standard out.
```argument1``` should be the name of the facility you're looking for. This string will be used to search through the AWS inventory's FQDNs of guardians.
```argument2``` is optional. If ommitted, it will default to "1". It must be a non-zero, non-negative integer. Use this argument if your search will return more than one result (for example, if a facility has two guardians and you want to specify the second).

### Example usage:
```get-mi broadmoo 2``` returns:
```mi-04430aafa83737aa4```

while

```get-mi broadmoo``` returns:
```mi-0211180472c0b50ba```

note that the program doesn't need the complete spelling of the facility to find an FQDN. It is also important to note that because of this, some common string fragments like "brookdale", "green", "oak", "guardian" etc. will return MANY results. Try to be specific with your search.

### Using this with streamtunnel:
This program can be especially useful for doing something like tunneling to a camera's RTSP stream. To use the result of ```get-mi``` as an argument for streamtunnel do:
```streamtunnel $(get-mi facility optional-arg) ip-addr```

### Example streamtunnel usage:
```streamtunnel $(get-mi broadmoo 2) 10.1.10.69```