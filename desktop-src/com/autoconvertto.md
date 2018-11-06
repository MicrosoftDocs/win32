---
title: AutoConvertTo
description: Specifies the automatic conversion of a given class of objects to a new class of objects.
ms.assetid: e34b799b-0d23-4034-ba79-49e92ec4dea7
keywords:
- AutoConvertTo registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# AutoConvertTo

Specifies the automatic conversion of a given class of objects to a new class of objects.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      AutoConvertTo = value
```

## Remarks

This is a **REG\_SZ** value that specifies the class identifier of the object to which the given object or class of objects should be converted.

This key is typically used to automatically convert files created by an older version of an application to a newer version of the application.

## Related topics

<dl> <dt>

[**OleDoAutoConvert**](/windows/desktop/api/Ole2/nf-ole2-oledoautoconvert)
</dt> <dt>

[**OleGetAutoConvert**](/windows/desktop/api/Ole2/nf-ole2-olegetautoconvert)
</dt> <dt>

[**OleSetAutoConvert**](/windows/desktop/api/Ole2/nf-ole2-olesetautoconvert)
</dt> </dl>

 

 




