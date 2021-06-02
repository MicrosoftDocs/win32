---
title: version-independent ProgID Key
description: Associates a ProgID with a CLSID. This key is used to determine the latest version of an object application.
ms.assetid: fb43c8d0-d923-487f-afdf-14fc29a71e0b
ms.topic: article
ms.date: 05/31/2018
---

# version-independent ProgID Key

Associates a ProgID with a CLSID. This key is used to determine the latest version of an object application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes
   <version-independent ProgID>
      CurVer = ProgID
```

## Remarks

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

The format for <*version-independent ProgID*> is <*program*>.<*component*>, separated by periods, no spaces, and no version number. The version-independent ProgID, like the ProgID, can be registered with a human-readable name.

*ProgID* is the ProgID of the latest installed version of the class.

Applications must register a version-independent programmatic identifier under the *version-independent ProgID* key. The version-independent ProgID refers to the application's class and does not change from version to version, instead remaining constant across all versionsâ€”for example, Microsoft Word Document. It is used with macro languages and refers to the currently installed version of the application's class. The version-independent ProgID must correspond to the name of the latest version of the object application.

For example, the version-independent ProgID is used when a container application creates a chart or table with a toolbar button. In this situation, the application can use the version-independent ProgID to determine the latest version of the needed object application.

The version-independent ProgID is stored and maintained solely by application code. When given the version-independent ProgID, the [**CLSIDFromProgID**](/windows/desktop/api/combaseapi/nf-combaseapi-clsidfromprogid) function returns the CLSID of the current version.

You can use [**CLSIDFromProgID**](/windows/desktop/api/combaseapi/nf-combaseapi-clsidfromprogid) and [**ProgIDFromCLSID**](/windows/desktop/api/combaseapi/nf-combaseapi-progidfromclsid) to convert between these two representations.

You can use [**IOleObject::GetUserType**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getusertype) or [**OleRegGetUserType**](/windows/desktop/api/Ole2/nf-ole2-olereggetusertype) to change the identifier to a displayable string.

If a custom handler is not used, the entry should be set to OLE32.DLL, as shown in the following example:

```
HKEY_CLASSES_ROOT\CLSID\{00000402-0000-0000-C000-000000000046}
   InprocHandler = ole32.dll
```

## Related topics

<dl> <dt>

[**CLSIDFromProgID**](/windows/desktop/api/combaseapi/nf-combaseapi-clsidfromprogid)
</dt> <dt>

[**ProgIDFromCLSID**](/windows/desktop/api/combaseapi/nf-combaseapi-progidfromclsid)
</dt> <dt>

[<ProgID> Key](-progid--key.md)
</dt> </dl>

 

 




