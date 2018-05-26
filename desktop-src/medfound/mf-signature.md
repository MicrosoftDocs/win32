---
Description: Contains a global revocation list (GRL) signature.
ms.assetid: 388a901c-6202-41cf-9c3d-f29d8ccca76b
title: MF\_SIGNATURE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SIGNATURE structure

Contains a global revocation list (GRL) signature.

## Syntax


```C++
typedef struct _MF_SIGNATURE {
  DWORD dwSignVer;
  DWORD cbSign;
  BYTE  rgSign[1];
} MF_SIGNATURE;
```



## Members

<dl> <dt>

**dwSignVer**
</dt> <dd>

The signature version number.

</dd> <dt>

**cbSign**
</dt> <dd>

The size of the signature in bytes.

</dd> <dt>

**rgSign**
</dt> <dd>

A byte array of size **cbSign** that contains the signature. The actual array size is larger than the size given in the structure declaration.

</dd> </dl>

## Remarks

This structure is not declared in an SDK header. To use this structure, add the declaration shown here to your source code.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[OPM Certificate Revocation](opm-certificate-revocation.md)
</dt> <dt>

[OPM Structures](opm-structures.md)
</dt> </dl>

 

 




