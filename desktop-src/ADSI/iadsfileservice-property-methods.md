---
title: IADsFileService Property Methods
description: The property methods of the IADsFileService interface get or set the properties described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1455df61-9218-450b-b956-1cf127364f24
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IADsFileService Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsFileService Property Methods
- IADsFileService.Description
- IADsFileService.get_Description
- IADsFileService.put_Description
- IADsFileService.MaxUserCount
- IADsFileService.get_MaxUserCount
- IADsFileService.put_MaxUserCount
api_location:
- Activeds.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IADsFileService Property Methods

The property methods of the [**IADsFileService**](/windows/win32/Iads/nn-iads-iadsfileservice?branch=master) interface get or set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Description**
</dt> <dd> <dl>

The description of the file service.

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

**MaxUserCount**
</dt> <dd> <dl>

The maximum number of users allowed on the service at any time.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MaxUserCount(
  [out] LONG* plMaxUserCount
);
HRESULT put_MaxUserCount(
  [in] LONG lMaxUserCount
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

You must go through the file service to access file shares, sessions, and resources on a computer.

## Examples

The following code example writes a description for and check the user limit of the file service.


```VB
Dim fs As IADsFileService
On Error GoTo Cleanup

' Bind to a file service object on "myComputer" in the local domain.
Set fs = GetObject("WinNT://myComputer/LanmanServer")

fs.Description = "WinNT file service."
n = fs.MaxUserCount
If n = -1 Then
   MsgBox "No limit has been imposed on number of users allowed."
Else
   MsgBox n & " users are allowed."
End If

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set fs = Nothing
```



The following code example writes a description for and check the user limit on a file service object.


```C++
HRESULT CheckFileService()
{
    IADsFileService *pFs = NULL;
    LPWSTR adsPath = L"WinNT://myComputer/LanmanServer";
    HRESULT hr = S_OK;
    long count = 0;

    hr = ADsGetObject(adsPath, IID_IADsFileService, (void**)&amp;pFs)
    if(FAILED(hr)) {goto Cleanup;}

    hr = pFs->put_Description(CComBSTR("WinNT File Service"));
    if(FAILED(hr)) {goto Cleanup;}

    hr = pFs->SetInfo();
    if(FAILED(hr)) {goto Cleanup;}

    hr = pFs->get_MaxUserCount(&amp;count);
    if(FAILED(hr)) {goto Cleanup;}

    if(count == -1) {
        printf("No limit has been imposed on the number of users.\n");
    } 
    else {
        printf("Number of allowed users are %d\n",count);
    }

Cleanup:
    if(pFs) pFs->Release();
    return S_OK;
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsFileService is defined as A89D1900-31CA-11CF-A98A-00AA006BC149<br/>      |



## See also

<dl> <dt>

[**IADsService**](/windows/win32/Iads/nn-iads-iadsservice?branch=master)
</dt> <dt>

[**IADsFileService**](/windows/win32/Iads/nn-iads-iadsfileservice?branch=master)
</dt> <dt>

[**IADsFileServiceOperations**](/windows/win32/Iads/nn-iads-iadsfileserviceoperations?branch=master)
</dt> <dt>

[**IADsServiceOperations**](/windows/win32/Iads/nn-iads-iadsserviceoperations?branch=master)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> </dl>

 

 





