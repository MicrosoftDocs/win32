---
title: IConfigAsfWriter2 ResetMultiPassState method
description: The ResetMultiPassState method resets the filter when a preprocessing encoding pass is canceled before it is completed.
ms.assetid: b6687af7-f3cd-4e92-9c76-dddff9063fa0
keywords:
- ResetMultiPassState method windows Media Format
- ResetMultiPassState method windows Media Format , IConfigAsfWriter2 interface
- IConfigAsfWriter2 interface windows Media Format , ResetMultiPassState method
topic_type:
- apiref
api_name:
- IConfigAsfWriter2.ResetMultiPassState
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter2::ResetMultiPassState method

The **ResetMultiPassState** method resets the filter when a preprocessing encoding pass is canceled before it is completed.

## Syntax


```C++
HRESULT ResetMultiPassState();
```



## Parameters

This method has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                         | Description                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | The method succeeded.<br/>                  |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl> | The filter was not in a stopped state.<br/> |



 

## Remarks

This method must be called to reset the internal state of the filter whenever a preprocessing encoding pass is canceled before the filter has received an **EC\_PREPROCESS\_COMPLETE** event. It is not necessary to call this method if the preprocessing encoding pass completes without errors.

## See also

<dl> <dt>

[**IConfigAsfWriter2 Interface**](/previous-versions/windows/desktop/legacy/dd743206(v=vs.85))
</dt> </dl>

 

