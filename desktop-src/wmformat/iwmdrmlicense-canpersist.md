---
title: IWMDRMLicense CanPersist method (Wmdrmsdk.h)
description: The CanPersist method queries whether the license can be persisted on in a local license store.
ms.assetid: 040b30d8-4e47-44a3-8b09-e81cc30e8a53
keywords:
- CanPersist method windows Media Format
- CanPersist method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , CanPersist method
topic_type:
- apiref
api_name:
- IWMDRMLicense.CanPersist
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicense::CanPersist method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CanPersist** method queries whether the license can be persisted on in a local license store.

## Syntax


```C++
HRESULT CanPersist(
  [out] BOOL *pfCanPersist
);
```



## Parameters

<dl> <dt>

*pfCanPersist* \[out\]
</dt> <dd>

TRUE indicates that the license can be persisted.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





