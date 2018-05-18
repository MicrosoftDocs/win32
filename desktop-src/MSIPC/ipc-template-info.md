---
title: IPC\_TEMPLATE\_INFO structure
description: Contains information for a template.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'b8cf52ae-b204-401c-9818-dcfdc03676eb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_TEMPLATE_INFO structure Active Directory Rights Management Services SDK 2.0", "PIPC_TEMPLATE_INFO structure pointer Active Directory Rights Management Services SDK 2.0", "PCIPC_TEMPLATE_INFO structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_TEMPLATE_INFO
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# IPC\_TEMPLATE\_INFO structure

Contains information for a template such as ID, locale, name, and description.

## Syntax


```C++
typedef struct _IPC_TEMPLATE_INFO {
  LPCWSTR wszID;
  LCID    lcid;
  LPCWSTR wszName;
  LPCWSTR wszDescription;
  LPCWSTR wszIssuerDisplayName;
  BOOL    fFromTemplate;
} IPC_TEMPLATE_INFO, *PIPC_TEMPLATE_INFO;typedef const IPC_TEMPLATE_INFO *PCIPC_TEMPLATE_INFO;
```



## Members

<dl> <dt>

**wszID**
</dt> <dd>

The template ID.

This member is read-only.

</dd> <dt>

**lcid**
</dt> <dd>

The locale ID for the template name and description.

This member, **lcid**, must be set to the locale ID of the template information of this structure instance. For more information about platform behavior regarding locale ID, see the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic.

</dd> <dt>

**wszName**
</dt> <dd>

The template name.

Do not include a colon (:) character or a semicolon (;) character in the string.

</dd> <dt>

**wszDescription**
</dt> <dd>

The template description.

Do not include a colon (:) character or a semicolon (;) character in the string.

</dd> <dt>

**wszIssuerDisplayName**
</dt> <dd>

The name of the RMS server that issued the template, in a format that can be displayed to the user.

This member is read-only.

</dd> <dt>

**fFromTemplate**
</dt> <dd>

Specifies whether the license was created directly from a template (for example, enumerated using [**IpcGetTemplateList**](ipcgettemplatelist.md)). The property is a **BOOL** and is **TRUE** if the license was created directly from a template, otherwise **FALSE**.

This member is read-only.

</dd> </dl>

## Remarks

When using this structure with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the following members are not required and are ignored:

-   **wszID**
-   **wszIssuerDisplayName**
-   **fFromTemplate**

When using this structure with [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) or [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the member **wszID** is returned as **NULL** when the license was not created directly from a template.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[Release notes](release-notes--rtm-.md)
</dt> </dl>

 

 





