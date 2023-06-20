---
title: IReferenceClock Unadvise method
description: The Unadvise method cancels a notification request.
ms.assetid: 9817a054-0c6c-402f-afb1-54748ff46a4b
keywords:
- Unadvise method windows Media Format
- Unadvise method windows Media Format , IReferenceClock interface
- IReferenceClock interface windows Media Format , Unadvise method
topic_type:
- apiref
api_name:
- IReferenceClock.Unadvise
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IReferenceClock::Unadvise method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Unadvise** method cancels a notification request.

## Syntax


```C++
HRESULT Unadvise(
   DWORD dwAdviseCookie
);
```



## Parameters

<dl> <dt>

*dwAdviseCookie* 
</dt> <dd>

Identifier of the request to remove. Use the value returned by AdviseTime in the pdwAdviseCookie parameter.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                             | Description                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The method succeeded.<br/>                    |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The identifier passed in does not exist.<br/> |



 

## See also

<dl> <dt>

[**IReferenceClock Interface**](ireferenceclock.md)
</dt> </dl>

 

 





