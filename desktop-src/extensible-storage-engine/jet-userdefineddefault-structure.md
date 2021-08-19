---
description: "Learn more about: JET_USERDEFINEDDEFAULT Structure"
title: JET_USERDEFINEDDEFAULT Structure
TOCTitle: JET_USERDEFINEDDEFAULT Structure
ms:assetid: 1f0a5419-9fae-4a93-a271-2f9772ecc996
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269200(v=EXCHG.10)
ms:contentKeyID: 32765503
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_USERDEFINEDDEFAULT Structure


_**Applies to:** Windows | Windows Server_

## JET_USERDEFINEDDEFAULT Structure

The **JET_USERDEFINEDDEFAULT** structure is specified in conjunction with JET_bitColumnUserDefinedDefault to give a new column a default value that is determined using a callback. This technique can be used to implement computed columns.

**Windows XP:** The **JET_USERDEFINEDDEFAULT** structure is introduced in Windows XP.

```cpp
    typedef struct tag_JET_USERDEFINEDDEFAULT {
      tchar* szCallback;
      unsigned char* pbUserData;
      unsigned long cbUserData;
      tchar* szDependantColumns;
    } JET_USERDEFINEDDEFAULT;
```

### Members

**szCallback**

The export name of the function that implements the callback in "module\!function" format.

The callback persists as a part of the column schema. The actual host executable and export name of the function must persist to enable the lookup of the true address of the function at run time.

The module name is the name of the host binary that contains the function. The function name is the name of the export for that function. These two pieces of information will be used by the database engine at runtime to locate the true address of the callback by executing a [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) call on the module name followed by a [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) call on the function name.

For example, if the callback were implemented in a DLL called MyCallback.DLL and that DLL were stored in C:\\MyApplication and the function implementing the callback were exported from the DLL as UserDefinedDefaultCallback, then the required string would be "C:\\MyApplication\\MyCallback.DLL\!UserDefinedDefaultCallback".

**Note**  Embedded "\!" characters in the module portion of the callback name are not supported.

It is highly recommended that you use a callback name that is not a function of the host architecture. For example, do not use exports decorated as stdcall (UserDefinedDefaultCallback@32) because this calling convention is only supported on x86 machines. If such a callback were used then the database could only be used on an x86 machine. An alias should be used to make a platform-agnostic export in this case.

It is highly recommended that you use the full path of the module name that is implementing the callback. If a relative path is used then the process that is hosting the database might be susceptible to attack by a rogue binary.

The application should pass only trusted callbacks to the database engine. The database engine will load the binary to verify its existence when the associated column is created. If the path to the binary is not validated or known to be trusted then it could attack the process that is hosting the database.

**pbUserData**

A self-contained block of user-defined data to be passed to the callback when invoked.The data block that is provided will persist as a part of the column schema. As a result, the data block must be entirely self-contained and cannot refer to any data that is outside the scope of the database.

If **pbUserData** is zero then the value of **cbUserData** is ignored. In this case, no user-defined data will be passed to the callback when invoked.

**cbUserData**

See **pbUserData**.

**szDependantColumns**

Reserved for future use.

This member should always be set to NULL.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_ USERDEFINEDDEFAULT_W</strong> (Unicode) and <strong>JET_ USERDEFINEDDEFAULT_A</strong> (ANSI).</p> | 



### See Also

[JET_CBTYP](./jet-cbtyp.md)  
[JET_COLUMNCREATE](./jet-columncreate-structure.md)  
[JET_COLUMNDEF](./jet-columndef-structure.md)
