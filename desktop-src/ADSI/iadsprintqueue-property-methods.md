---
title: IADsPrintQueue Property Methods (Iads.h)
description: The property methods of the IADsPrintQueue interface get or set the properties described in the following table. For more information, see Interface Property Methods.
ms.assetid: 7f5b4200-65c8-4230-8561-ad4fefb391f3
ms.tgt_platform: multiple
keywords:
- IADsPrintQueue Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsPrintQueue Property Methods
- IADsPrintQueue.BannerPage
- IADsPrintQueue.get_BannerPage
- IADsPrintQueue.put_BannerPage
- IADsPrintQueue.Datatype
- IADsPrintQueue.get_Datatype
- IADsPrintQueue.put_Datatype
- IADsPrintQueue.DefaultJobPriority
- IADsPrintQueue.get_DefaultJobPriority
- IADsPrintQueue.put_DefaultJobPriority
- IADsPrintQueue.Description
- IADsPrintQueue.get_Description
- IADsPrintQueue.put_Description
- IADsPrintQueue.HostComputer
- IADsPrintQueue.get_HostComputer
- IADsPrintQueue.put_HostComputer
- IADsPrintQueue.Location
- IADsPrintQueue.get_Location
- IADsPrintQueue.put_Location
- IADsPrintQueue.Model
- IADsPrintQueue.get_Model
- IADsPrintQueue.put_Model
- IADsPrintQueue.PrintDevices
- IADsPrintQueue.get_PrintDevices
- IADsPrintQueue.put_PrintDevices
- IADsPrintQueue.PrinterPath
- IADsPrintQueue.get_PrinterPath
- IADsPrintQueue.put_PrinterPath
- IADsPrintQueue.PrintProcessor
- IADsPrintQueue.get_PrintProcessor
- IADsPrintQueue.put_PrintProcessor
- IADsPrintQueue.Priority
- IADsPrintQueue.get_Priority
- IADsPrintQueue.put_Priority
- IADsPrintQueue.StartTime
- IADsPrintQueue.get_StartTime
- IADsPrintQueue.put_StartTime
- IADsPrintQueue.UntilTime
- IADsPrintQueue.get_UntilTime
- IADsPrintQueue.put_UntilTime
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsPrintQueue Property Methods

The property methods of the [**IADsPrintQueue**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue) interface get or set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**BannerPage**
</dt> <dd> <dl>

The file system path that points to the banner page used to separate print jobs. If **NULL**, no banner page is used.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BannerPage(
  [out] BSTR* pbstrBannerPage
);
HRESULT put_BannerPage(
  [in] BSTR bstrBannerPage
);
```


</dt> </dl> </dd> <dt>

**Datatype**
</dt> <dd> <dl>

The data type that can be processed by this queue.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Datatype(
  [out] BSTR* pbstrDatatype
);
HRESULT put_Datatype(
  [in] BSTR bstrDatatype
);
```


</dt> </dl> </dd> <dt>

**DefaultJobPriority**
</dt> <dd> <dl>

The default priority assigned to each print job.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DefaultJobPriority(
  [out] LONG* plDefaultJobPriority
);
HRESULT put_DefaultJobPriority(
  [in] BSTR lDefaultJobPriority
);
```


</dt> </dl> </dd> <dt>

**Description**
</dt> <dd> <dl>

The text description of this print queue.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Description(
  [out] BSTR* pbstrDescription
);
HRESULT put_Description(
  [in] BSTR bstrDescription
);
```


</dt> </dl> </dd> <dt>

**HostComputer**
</dt> <dd> <dl>

The ADsPath string that references the host computer.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_HostComputer(
  [out] BSTR* pbstrHostComputer
);
HRESULT put_HostComputer(
  [in] BSTR bstrHostComputer
);
```


</dt> </dl> </dd> <dt>

**Location**
</dt> <dd> <dl>

The location of the queue as described by an administrator.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Location(
  [out] BSTR* pbstrLocation
);
HRESULT put_Location(
  [in] BSTR bstrLocation
);
```


</dt> </dl> </dd> <dt>

**Model**
</dt> <dd> <dl>

The name of the driver used by this print queue.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Model(
  [out] BSTR* pbstrModel
);
HRESULT put_Model(
  [in] BSTR bstrModel
);
```


</dt> </dl> </dd> <dt>

**PrintDevices**
</dt> <dd> <dl>

A SAFEARRAY of **BSTR** that contains the names of the print devices to which this print queue spools jobs.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PrintDevices(
  [out] VARIANT* pvPrintDevices
);
HRESULT put_PrintDevices(
  [in] VARIANT vPrintDevices
);
```


</dt> </dl> </dd> <dt>

**PrinterPath**
</dt> <dd> <dl>

The string that references the path by which a shared printer can be accessed.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PrinterPath(
  [out] BSTR* pbstrPrinterPath
);
HRESULT put_PrinterPath(
  [in] BSTR bstrPrinterPath
);
```


</dt> </dl> </dd> <dt>

**PrintProcessor**
</dt> <dd> <dl>

The print processor associated with this queue.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PrintProcessor(
  [out] BSTR* pbstrPrintProcessor
);
HRESULT put_PrintProcessor(
  [in] BSTR bstrPrintProcessor
);
```


</dt> </dl> </dd> <dt>

**Priority**
</dt> <dd> <dl>

The priority of this printer object job queue for any connected devices. All jobs in higher priority print queue objects will be processed first.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Priority(
  [out] LONG* plPriority
);
HRESULT put_Priority(
  [in] LONG lPriority
);
```


</dt> </dl> </dd> <dt>

**StartTime**
</dt> <dd> <dl>

The time when the queue should begin processing jobs. The date portion of the time is ignored.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StartTime(
  [out] DATE* pdateStartTime
);
HRESULT put_StartTime(
  [in] DATE dateStartTime
);
```


</dt> </dl> </dd> <dt>

**UntilTime**
</dt> <dd> <dl>

The time when the queue should stop processing jobs.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UntilTime(
  [out] DATE* pdateUntilTime
);
HRESULT put_UntilTime(
  [in] DATE dateUntilTime
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example shows how to determine if a specified printer is online or offline.


```VB
Dim pq As IADsPrintQueue
Dim pqo As IADsPrintQueueOperations
On Error GoTo Cleanup
 
Set pq = GetObject("WinNT://aMachine/aPrinter")
Set pqo = pq
If pqo.status = ADS_PRINTER_OFFLINE Then
    MsgBox pq.Model & "@" & pq.Location & is offline."
Else
    MsgBox pq.Model & "@" & pq.Location & is online."
End If

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set pq = Nothing
    Set pqo = Nothing
```



The following code example shows how to determine if a specified printer is online or offline.


```C++
IADsPrintQueue *pq = NULL;
HRESULT hr = S_OK;
IADsPrintQueueOperations *pqo = NULL;
BSTR model = NULL;
BSTR location = NULL;

LPWSTR adsPath = L"WinNT://aMachine/aPrinter";
hr = ADsGetObject(adsPath,
                  IID_IADsPrintQueue,
                  (void**)&pq);
if(FAILED(hr)) {goto Cleanup;}


hr = pq->QueryInterface(IID_IADsPrintQueueOperations,(void**)&pqo);
if(FAILED(hr)) {goto Cleanup;}

long status;
hr = pqo->get_Status(&status);
if(FAILED(hr)) {goto Cleanup;}

hr = pq->get_Model(&model);
if(FAILED(hr)) {goto Cleanup;}

hr =pq->get_Location(&location);
if(FAILED(hr)) {goto Cleanup;}

if(status == ADS_PRINTER_OFFLINE) 
{
    printf("%S @ %S is offline.\n",model,location);
} 
else 
{
    printf("%S @ %S is online.\n",model,location);
}


Cleanup:
    SysFreeString(model);
    SysFreeString(location);
    if(pq) pq->Release();
    if(pqo) pqo->Release();
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsPrintQueue is defined as B15160D0-1226-11CF-A985-00AA006BC149<br/>       |



## See also

<dl> <dt>

[**IADsPrintQueue**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> </dl>

 

 





