---
title: INapComponentConfig2 InvokeUIFromConfigBlob method (NapCommon.h)
description: Is implemented by system health validators (SHVs) as needed to load the configuration of a remote or local machine in memory and display a UI that allows manipulation of the configuration data.
ms.assetid: 9c012690-6751-4a47-8683-74abac610c77
keywords:
- InvokeUIFromConfigBlob method NAP
- InvokeUIFromConfigBlob method NAP , INapComponentConfig2 interface
- INapComponentConfig2 interface NAP , InvokeUIFromConfigBlob method
topic_type:
- apiref
api_name:
- INapComponentConfig2.InvokeUIFromConfigBlob
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig2::InvokeUIFromConfigBlob method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **InvokeUIFromConfigBlob** method is implemented by system health validators (SHVs) as needed to load the configuration of a remote or local machine in memory and display a UI that allows manipulation of the configuration data. The configuration component must support the usage of [**INapComponentConfig**](inapcomponentconfig.md) through DCOM.

## Syntax


```C++
HRESULT InvokeUIFromConfigBlob(
  [in, unique] HWND   hwndParent,
  [in]         UINT16 inbCount,
  [in]         BYTE   *inData,
  [out]        UINT16 *outbCount,
  [out]        BYTE   **outdata,
  [out]        BOOL   *fConfigChanged
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

A handle to the parent or owner window. A valid window handle must be supplied.

</dd> <dt>

*inbCount* \[in\]
</dt> <dd>

The size, in bytes, of *inData*.

</dd> <dt>

*inData* \[in\]
</dt> <dd>

A pointer to a buffer that stores the initial configuration data. This data is exported from the remote or local machine.

</dd> <dt>

*outbCount* \[out\]
</dt> <dd>

The size, in bytes, of *outdata*.

</dd> <dt>

*outdata* \[out\]
</dt> <dd>

A pointer to a buffer that stores configuration data changed by the SHV configuration user interface. This data is imported by the remote or local machine.

</dd> <dt>

*fConfigChanged* \[out\]
</dt> <dd>

A pointer to a **BOOL** that is set to **TRUE** if the configuration was changed during the UI operation and **FALSE** otherwise.

</dd> </dl>

## Return value

Returns S\_OK if successful, or one of the standard Windows error codes.

## Remarks

If used for a local machine, this function can be used for per policy SHV configuration. It provides a way to invoke an SHV UI and edit an existing SHV configuration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig2**](inapcomponentconfig2.md)
</dt> </dl>

 

 





