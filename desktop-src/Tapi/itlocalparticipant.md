---
Description: The ITLocalParticipant interface is exposed on the stream object when the IPConf MSP supports the call.
ms.assetid: 64965ae2-e30b-4353-a502-f96018da71a5
title: ITLocalParticipant interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITLocalParticipant interface

The **ITLocalParticipant** interface is exposed on the stream object when the IPConf MSP supports the call. The MSP implements methods that allow an application to get and set participant information. The **ITLocalParticipant** interface is created by calling **QueryInterface** on [**ITStream**](https://msdn.microsoft.com/en-us/library/ms732390(v=VS.85).aspx).

## Members

The **ITLocalParticipant** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITLocalParticipant** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITLocalParticipant** interface has these methods.



| Method                                                                                     | Description                                                                            |
|:-------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**get\_LocalParticipantTypedInfo**](itlocalparticipant-get-localparticipanttypedinfo.md) | Gets participant information, such as e-mail name or geographical location.<br/> |
| [**put\_LocalParticipantTypedInfo**](itlocalparticipant-put-localparticipanttypedinfo.md) | Sets participant information.<br/>                                               |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITStream**](https://msdn.microsoft.com/en-us/library/ms732390(v=VS.85).aspx)
</dt> </dl>

 

 




