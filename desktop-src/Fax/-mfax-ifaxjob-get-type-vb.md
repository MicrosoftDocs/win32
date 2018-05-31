---
Description: The Type property is a number that describes the type of fax job represented by the object.
ms.assetid: 04d3f8e2-cf49-4497-bf89-7b9f777923b2
title: FaxJob.Type property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.Type property

The **Type** property is a number that describes the type of fax job represented by the object.

This property is read-only.

## Syntax


```VB
Property Type As Long
```



## Property value

A **Long** that receives a numeric value that describes the type of the specified fax job. This value can be one of the following job types.

<dt>

<span id="JT_SEND"></span><span id="jt_send"></span>

<span id="JT_SEND"></span><span id="jt_send"></span>**JT\_SEND** (JT\_SEND)


</dt> <dd>

The job is an outgoing fax transmission.

</dd> <dt>

<span id="JT_RECEIVE"></span><span id="jt_receive"></span>

<span id="JT_RECEIVE"></span><span id="jt_receive"></span>**JT\_RECEIVE** (JT\_RECEIVE)


</dt> <dd>

The job is an incoming fax transmission.

</dd> <dt>

<span id="JT_UNKNOWN"></span><span id="jt_unknown"></span>

<span id="JT_UNKNOWN"></span><span id="jt_unknown"></span>**JT\_UNKNOWN** (JT\_UNKNOWN)


</dt> <dd>

The job type is unknown. This value indicates that the fax server has not yet scheduled the job.

</dd> <dt>

<span id="JT_ROUTING"></span><span id="jt_routing"></span>

<span id="JT_ROUTING"></span><span id="jt_routing"></span>**JT\_ROUTING** (JT\_ROUTING)


</dt> <dd>

The fax server tried to route the fax transmission, but routing failed. The fax server will attempt to route the job again.

</dd> <dt>

<span id="JT_FAIL_RECEIVE"></span><span id="jt_fail_receive"></span>

<span id="JT_FAIL_RECEIVE"></span><span id="jt_fail_receive"></span>**JT\_FAIL\_RECEIVE** (JT\_FAIL\_RECEIVE)


</dt> <dd>

The fax server did not route the fax because it did not receive the entire transmission. The fax server saves the partial transmission in a temporary directory.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob)
</dt> <dt>

[**IFaxJobs**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjobs)
</dt> </dl>

 

 




