---
title: IrDA and IAS
description: Only limited access to the IAS database is available through Windows Sockets, however, the IAS database is not normally used by applications.
ms.assetid: 190518b3-2c64-445a-a1a2-24ad56ad77c7
keywords:
- IrDA and IAS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrDA and IAS

Only limited access to the IAS database is available through Windows Sockets, however, the IAS database is not normally used by applications. The IAS database exists to support connections to non-Windows devices that are not compliant with Windows Sockets and IrDA conventions.

The following structure, **IAS\_SET**, is used with the Windows Sockets [**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476) function and **IRLMP\_IAS\_SET** to manage the local IAS database:

``` syntax
typedef struct _IAS_SET
{
char    irdaClassName[IAS_MAX_CLASSNAME];
char    irdaAttribName[IAS_MAX_ATTRIBNAME];
u_long    irdaAttribType;
union
{
LONG irdaAttribInt;
struct
{
u_short    Len;
u_char    OctetSeq[IAS_MAX_OCTET_STRING];
} irdaAttribOctetSeq;
struct
{
u_char    Len;
u_char    CharSet;
u_char    UsrStr[IAS_MAX_USER_STRING];
        } irdaAttribUsrStr;
} irdaAttribute;
} IAS_SET, *PIAS_SET, FAR *LPIAS_SET;
```

The **IAS\_QUERY** structure, defined below, is used with the [**getsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms738544) function and **IRLMP\_IAS\_QUERY** to query the IAS database on a peer:

``` syntax
typedef struct _WINDOWS_IAS_QUERY
{
u_char    irdaDeviceID[4];
char    irdaClassName[IAS_MAX_CLASSNAME];
char    irdaAttribName[IAS_MAX_ATTRIBNAME];
u_long    irdaAttribType;
union
{
LONG    irdaAttribInt;
struct
{
u_long    Len;
u_char    OctetSeq[IAS_MAX_OCTET_STRING];
} irdaAttribOctetSeq;
struct
{
u_long  Len;
u_long    CharSet;
u_char    UsrStr[IAS_MAX_USER_STRING];
} irdaAttribUsrStr;
} irdaAttribute;
} IAS_QUERY, *PIAS_QUERY, FAR *LPIAS_QUERY;
```

 

 




