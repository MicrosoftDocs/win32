---
title: IWMDRMLicense GetNext method (Wmdrmsdk.h)
description: The GetNext method loads the information about the next item in the list.
ms.assetid: 5ef91751-2883-4a8e-9908-7a6dfe6d2af3
keywords:
- GetNext method windows Media Format
- GetNext method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetNext method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetNext
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::GetNext method

The **GetNext** method loads the information about the next item in the list.

## Syntax


```C++
HRESULT GetNext();
```



## Parameters

This method has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                | Description                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NS\_E\_DRM\_RIV\_TOO\_SMALL**</dt> </dl> | An updated content revocation list is needed.<br/> |
| <dl> <dt>**ERROR\_NO\_MORE\_ITEMS**</dt> </dl>      | There are no more items in the list.<br/>          |
| <dl> <dt>**S\_OK**</dt> </dl>                       | The method succeeded.<br/>                         |



 

## Remarks

The methods of the [**IWMDRMLicense**](iwmdrmlicense.md) interface provide data about a single license at a time. The underlying object contains a list of one or more licenses. When you call this method, the interface moves its internal references to the next license in the list.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





