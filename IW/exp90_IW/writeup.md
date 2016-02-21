$)'txtt5678.01234g67890a23456l89012f45678'01234(67890c23456n89012y45678S01234e67890l23456i89012F45678d01234a67890e23456r89012.45678s01234f67890=23456a01234
<Buffer 49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d>
$aa
<Buffer 49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d>
$echo '49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d' | xxd -r -p
[SyntaxError: Unexpected token ILLEGAL]
$^C      
root@bkthpc:~/Bureau/CTF/ctf# echo '49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d' | xxd -r -p
IW{Shocked-for-nothing!}

# Exp90

## Description
```
We are given an IP address and a port to connect to, upon connecting we juste have a greeting message and what seems to be an interepreter
```

## Solution

After poking around, we could see that the interpreter did not have a straightforward behavior.
The error messages seemed to indicate that it was a javascript interpreter (most likely node.js).

We first tried to do some simple variable declaration such as a=2. After testing many things it appeared to us that the interpreter was reading backwards and only took some characters to form the string to evaluate.

For example in order to declare a=2, you would need to input 22==aa

Knowing that it was most likely node.js and the previous challenges had flag.txt file in the same directory we tried to read the file

In node.js this would be equivalent to:

```
fs=require('fs')
a=fs.readFileSync('flag.txt')
```

We did not script anything or tried to had the formula used by the interpreter, instead we what we did is try to supply an integer that was interpreted to a number with as many digits as the number of chars in what wanted to be interpreted. And from that, we replaced the number that were output by the letters:

We ended up with the following

```
fs=require('fs') => )'sf45678'01234(67890e23456r89012i45678u01234q67890e23456r89012=45678s01234f67890
a=fs.readFileSync('flag.txt') => 'txtt5678.01234g67890a23456l89012f45678'01234(67890c23456n89012y45678S01234e67890l23456i89012F45678d01234a67890e23456r89012.45678s01234f67890=23456a01234
```



## Results
```
Welcome and have fun!
$)'sf45678'01234(67890e23456r89012i45678u01234q67890e23456r89012=45678s01234f67890
{ Stats: [Function],
  F_OK: 0,
  R_OK: 4,
  W_OK: 2,
  X_OK: 1,
  access: [Function],
  accessSync: [Function],
  exists: [Function],
  existsSync: [Function],
  readFile: [Function],
  readFileSync: [Function],
  close: [Function],
  closeSync: [Function],
  open: [Function],
  openSync: [Function],
  read: [Function],
  readSync: [Function],
  write: [Function],
  writeSync: [Function],
  rename: [Function],
  renameSync: [Function],
  truncate: [Function],
  truncateSync: [Function],
  ftruncate: [Function],
  ftruncateSync: [Function],
  rmdir: [Function],
  rmdirSync: [Function],
  fdatasync: [Function],
  fdatasyncSync: [Function],
  fsync: [Function],
  fsyncSync: [Function],
  mkdir: [Function],
  mkdirSync: [Function],
  readdir: [Function],
  readdirSync: [Function],
  fstat: [Function],
  lstat: [Function],
  stat: [Function],
  fstatSync: [Function],
  lstatSync: [Function],
  statSync: [Function],
  readlink: [Function],
  readlinkSync: [Function],
  symlink: [Function],
  symlinkSync: [Function],
  link: [Function],
  linkSync: [Function],
  unlink: [Function],
  unlinkSync: [Function],
  fchmod: [Function],
  fchmodSync: [Function],
  chmod: [Function],
  chmodSync: [Function],
  fchown: [Function],
  fchownSync: [Function],
  chown: [Function],
  chownSync: [Function],
  _toUnixTimestamp: [Function: toUnixTimestamp],
  utimes: [Function],
  utimesSync: [Function],
  futimes: [Function],
  futimesSync: [Function],
  writeFile: [Function],
  writeFileSync: [Function],
  appendFile: [Function],
  appendFileSync: [Function],
  watch: [Function],
  watchFile: [Function],
  unwatchFile: [Function],
  realpathSync: [Function: realpathSync],
  realpath: [Function: realpath],
  createReadStream: [Function],
  ReadStream: 
   { [Function: ReadStream]
     super_: 
      { [Function: Readable]
        ReadableState: [Function: ReadableState],
        super_: [Object],
        _fromList: [Function: fromList] } },
  FileReadStream: 
   { [Function: ReadStream]
     super_: 
      { [Function: Readable]
        ReadableState: [Function: ReadableState],
        super_: [Object],
        _fromList: [Function: fromList] } },
  createWriteStream: [Function],
  WriteStream: 
   { [Function: WriteStream]
     super_: { [Function: Writable] WritableState: [Function: WritableState], super_: [Object] } },
  FileWriteStream: 
   { [Function: WriteStream]
     super_: { [Function: Writable] WritableState: [Function: WritableState], super_: [Object] } } }
$)'txtt5678.01234g67890a23456l89012f45678'01234(67890c23456n89012y45678S01234e67890l23456i89012F45678d01234a67890e23456r89012.45678s01234f67890=23456a01234
<Buffer 49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d>

echo '49 57 7b 53 68 6f 63 6b 65 64 2d 66 6f 72 2d 6e 6f 74 68 69 6e 67 21 7d' | xxd -r -p
IW{Shocked-for-nothing!}
```
