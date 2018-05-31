---
title: IVMSecurity FindEntry method
description: The FindEntry method finds an existing access control entry.
ms.assetid: d004223c-f4fd-465a-b895-4d82c27a46a1
keywords:
- FindEntry method Virtual Server
- FindEntry method Virtual Server , IVMSecurity interface
- IVMSecurity interface Virtual Server , FindEntry method
- FindEntry method Virtual Server , VMSecurity interface
- VMSecurity interface Virtual Server , FindEntry method
topic_type:
- apiref
api_name:
- IVMSecurity.FindEntry
- VMSecurity.FindEntry
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

# IVMSecurity::FindEntry method

The **FindEntry** method finds an existing access control entry.

## Syntax


```C++
HRESULT FindEntry(
  [in]  BSTR               nameOrSid,
  [in]  VMAccessRightsType type,
  [out] IVMAccessRights    **foundEntry
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

*foundEntry* \[out\]
</dt> <dd>

The access control entry.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                                                                       |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt> **S\_FALSE**</dt> </dl>           | No entry with the specified name and type was found.<br/>                                   |
| <dl> <dt> **E\_POINTER**</dt> </dl>         | The parameter *nameOrSid* or *foundEntry* was null.<br/>                                    |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>      | An invalid value was specified for parameter *type*.<br/>                                   |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



 

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

 

 





