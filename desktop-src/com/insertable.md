---
title: Insertable (CLSID Key)
description: Indicates that objects of this class should appear in the Insert Object dialog box list box when used by COM container applications.
ms.assetid: 908cbfc4-ebf8-454e-b2e5-34449de60e7f
keywords:
- Insertable registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Insertable (CLSID Key)

Indicates that objects of this class should appear in the **Insert Object** dialog box list box when used by COM container applications.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Insertable
```

## Remarks

This key is a required entry for 32-bit COM applications whose objects can be inserted into existing 16-bit applications. Existing 16-bit applications look in the registry for this key, which informs the application that the server supports embeddings. If the **Insertable** key exists, 16-bit applications may also attempt to verify that the server exists on the machine. 16-bit applications typically retrieve the value of the [**LocalServer**](localserver.md) key from the class and check to see whether it is a valid file on the system. Therefore, for a 32-bit application to be insertable by a 16-bit application, the 32-bit application should register the **LocalServer** subkey in addition to registering [**LocalServer32**](localserver32.md).

Used with controls, this entry indicates that an object can act only as an in-place embedded object with no special control features. Objects that have this key appear in the **Insert Object** dialog box for their container. When used with controls, this entry also indicates the control has been tested with non-control containers. This entry is also optional and can be omitted when a control is not designed to work with older containers that do not understand controls.

> [!Note]  
> This key is not present for internal classes like the moniker classes.

 

## Related topics

<dl> <dt>

[**<ProgID>**](-progid--key.md)
</dt> </dl>

 

 




