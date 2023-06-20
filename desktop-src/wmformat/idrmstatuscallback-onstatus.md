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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IDRMStatusCallback::OnStatus method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





