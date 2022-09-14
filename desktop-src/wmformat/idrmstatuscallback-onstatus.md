---
title: IDRMStatusCallback OnStatus method
description: The OnStatus method receives status messages from asynchronous DRM processes.
ms.assetid: 2a128088-0924-4c54-b08d-a1c7ea91e541
keywords:
- OnStatus method windows Media Format
- OnStatus method windows Media Format , IDRMStatusCallback interface
- IDRMStatusCallback interface windows Media Format , OnStatus method
topic_type:
- apiref
api_name:
- IDRMStatusCallback.OnStatus
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IDRMStatusCallback::OnStatus method

The **OnStatus** method receives status messages from asynchronous DRM processes.

## Syntax


```C++
HRESULT OnStatus(
  [in] MSDRM_STATUS      Status,
  [in] HRESULT           hr,
  [in] DRM_ATTR_DATATYPE dwType,
  [in] BYTE              *pValue,
  [in] void              *pvContext
);
```



## Parameters

<dl> <dt>

*Status* \[in\]
</dt> <dd>

Status code. Message codes are defined in the **MSDRM\_STATUS** enumeration type.

</dd> <dt>

*hr* \[in\]
</dt> <dd>

Return code that supports the status message.

</dd> <dt>

*dwType* \[in\]
</dt> <dd>

Type of the data pointed to by *pValue*. Set to one of the values of the [**DRM\_ATTR\_DATATYPE**](drm-attr-datatype.md) enumeration.

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Pointer to data related to the status message. The type of data is determined by the value of the *dwType* parameter. For more information, see the [**DRM\_ATTR\_DATATYPE**](drm-attr-datatype.md) enumeration.

</dd> <dt>

*pvContext* \[in\]
</dt> <dd>

Optional parameter that can be used to identify the object that sent the message. By setting *pvContext* when you register this callback, you can use the same callback to handle multiple asynchronous processes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## See also

<dl> <dt>

[**DRM\_ATTR\_DATATYPE**](drm-attr-datatype.md)
</dt> <dt>

[**IDRMStatusCallback Interface**](idrmstatuscallback.md)
</dt> </dl>

 

 





