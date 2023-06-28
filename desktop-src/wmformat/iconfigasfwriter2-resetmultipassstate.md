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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter2::ResetMultiPassState method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

