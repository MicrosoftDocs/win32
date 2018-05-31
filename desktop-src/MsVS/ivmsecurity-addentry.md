---
title: IVMSecurity AddEntry method
description: The AddEntry method adds a new access control entry. The new access control entry has no rights enabled.
ms.assetid: 75dc94d6-c800-4961-bf59-3307593fa30b
keywords:
- AddEntry method Virtual Server
- AddEntry method Virtual Server , IVMSecurity interface
- IVMSecurity interface Virtual Server , AddEntry method
- AddEntry method Virtual Server , VMSecurity interface
- VMSecurity interface Virtual Server , AddEntry method
topic_type:
- apiref
api_name:
- IVMSecurity.AddEntry
- VMSecurity.AddEntry
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMSecurity::AddEntry method

The **AddEntry** method adds a new access control entry. The new access control entry has no rights enabled.

## Syntax


```C++
HRESULT AddEntry(
  [in]  BSTR               nameOrSid,
  [in]  VMAccessRightsType type,
  [out] IVMAccessRights    **newEntry
);
```



## Parameters

<dl> <dt>

*nameOrSid* \[in\]
</dt> <dd>

The account name or SID.

</dd> <dt>

*type* \[in\]
</dt> <dd>

The type of access control entry.

</dd> <dt>

*newEntry* \[out\]
</dt> <dd>

The new access control entry.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                     | Description                                                                        |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                           | The operation was successful.<br/>                                           |
| <dl> <dt> **E\_POINTER**</dt> </dl>                      | The *nameOrSid* or *newEntry* parameter was null.<br/>                       |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                   | An invalid value was specified for the *nameOrSid* or *type* parameter.<br/> |
| <dl> <dt>**VM\_E\_SECURITY\_DUPLICATE\_USER**</dt> </dl> | An entry with the same name and type already exists.<br/>                    |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>              | An unknown error has occurred.<br/>                                          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRights**](ivmaccessrights.md)
</dt> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> <dt>

[**VMAccessRightsType**](vmaccessrightstype.md)
</dt> </dl>

 

 





