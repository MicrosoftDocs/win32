---
title: IADsPrintQueueOperations Property Methods (Iads.h)
description: The property methods of the IADsPrintQueueOperations interface read and write the properties listed in the following list. For more information about property methods, see Interface Property Methods.
ms.assetid: a4e6bac5-5d52-4492-b48e-f051fec6158c
ms.tgt_platform: multiple
keywords:
- IADsPrintQueueOperations Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsPrintQueueOperations Property Methods
- IADsPrintQueueOperations.Status
- IADsPrintQueueOperations.get_Name
- IADsPrintQueueOperations.put_Name
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsPrintQueueOperations Property Methods

The property methods of the [**IADsPrintQueueOperations**](/windows/desktop/api/Iads/nn-iads-iadsprintqueueoperations) interface read and write the properties listed in the following list. For more information about property methods, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Status**
</dt> <dd> <dl>

Current status of the print queue operations. The valid status code values are listed in the following list.

<dt>

<span id="ADS_PRINTER_PAUSED"></span><span id="ads_printer_paused"></span>

**ADS\_PRINTER\_PAUSED** (0x00000001)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PENDING_DELETION"></span><span id="ads_printer_pending_deletion"></span>

**ADS\_PRINTER\_PENDING\_DELETION** (0x00000002)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_ERROR"></span><span id="ads_printer_error"></span>

**ADS\_PRINTER\_ERROR** (0x00000003)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PAPER_JAM"></span><span id="ads_printer_paper_jam"></span>

**ADS\_PRINTER\_PAPER\_JAM** (0x00000004)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PAPER_OUT"></span><span id="ads_printer_paper_out"></span>

**ADS\_PRINTER\_PAPER\_OUT** (0x00000005)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_MANUAL_FEED"></span><span id="ads_printer_manual_feed"></span>

**ADS\_PRINTER\_MANUAL\_FEED** (0x00000006)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PAPER_PROBLEM"></span><span id="ads_printer_paper_problem"></span>

**ADS\_PRINTER\_PAPER\_PROBLEM** (0x00000007)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_OFFLINE"></span><span id="ads_printer_offline"></span>

**ADS\_PRINTER\_OFFLINE** (0x00000008)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_IO_ACTIVE"></span><span id="ads_printer_io_active"></span>

**ADS\_PRINTER\_IO\_ACTIVE** (0x00000100)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_BUSY"></span><span id="ads_printer_busy"></span>

**ADS\_PRINTER\_BUSY** (0x00000200)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PRINTING"></span><span id="ads_printer_printing"></span>

**ADS\_PRINTER\_PRINTING** (0x00000400)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_OUTPUT_BIN_FULL"></span><span id="ads_printer_output_bin_full"></span>

**ADS\_PRINTER\_OUTPUT\_BIN\_FULL** (0x00000800)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_NOT_AVAILABLE"></span><span id="ads_printer_not_available"></span>

**ADS\_PRINTER\_NOT\_AVAILABLE** (0x00001000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_WAITING"></span><span id="ads_printer_waiting"></span>

**ADS\_PRINTER\_WAITING** (0x00002000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PROCESSING"></span><span id="ads_printer_processing"></span>

**ADS\_PRINTER\_PROCESSING** (0x00004000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_INITIALIZING"></span><span id="ads_printer_initializing"></span>

**ADS\_PRINTER\_INITIALIZING** (0x00008000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_WARMING_UP"></span><span id="ads_printer_warming_up"></span>

**ADS\_PRINTER\_WARMING\_UP** (0x00010000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_TONER_LOW"></span><span id="ads_printer_toner_low"></span>

**ADS\_PRINTER\_TONER\_LOW** (0x00020000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_NO_TONER"></span><span id="ads_printer_no_toner"></span>

**ADS\_PRINTER\_NO\_TONER** (0x00040000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_PAGE_PUNT"></span><span id="ads_printer_page_punt"></span>

**ADS\_PRINTER\_PAGE\_PUNT** (0x00080000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_USER_INTERVENTION"></span><span id="ads_printer_user_intervention"></span>

**ADS\_PRINTER\_USER\_INTERVENTION** (0x00100000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_OUT_OF_MEMORY"></span><span id="ads_printer_out_of_memory"></span>

**ADS\_PRINTER\_OUT\_OF\_MEMORY** (0x00200000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_DOOR_OPEN"></span><span id="ads_printer_door_open"></span>

**ADS\_PRINTER\_DOOR\_OPEN** (0x00400000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_SERVER_UNKNOWN"></span><span id="ads_printer_server_unknown"></span>

**ADS\_PRINTER\_SERVER\_UNKNOWN** (0x00800000)


</dt> <dd></dd> <dt>

<span id="ADS_PRINTER_POWER_SAVE"></span><span id="ads_printer_power_save"></span>

**ADS\_PRINTER\_POWER\_SAVE** (0x01000000)


</dt> <dd></dd> </dl> <dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Name(
  [out] LONG* pbstrName
);
HRESULT put_Name(
  [in] LONG bstrName
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following Visual Basic code example verifies that a printer is jammed.


```VB
Dim pqo As IADsPrintQueueOperations
Set pqo = GetObject("WinNT://aMachine/aPrinter")
If pqo.Status = ADS_PRINTER_PAPER_JAM Then
MsgBox "Your printer is jammed."
End If
```



The following C++ code example verifies that a printer is jammed.


```C++
IADsPrintQueueOperations *pqo;
HRESULT hr = ADsGetObject(L"WinNT://aMachine/aPrinter",
IID_IADsPrintQueueOperations,
(void**)&pqo)
long status;
hr = pqo->get_Status(&status);
if(status = ADS_PRINTER_PAPER_JAM) {
printf("Your printer is jammed.\n");
}
hr = pqo->Release();
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                              |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl>     |
| IID<br/>                      | IID\_IADsPrintQueueOperations is defined as 124BE5C0-156E-11CF-A986-00AA006BC149<br/> |



## See also

<dl> <dt>

[**IADsPrintQueue**](/windows/desktop/api/Iads/nn-iads-iadsprintqueue)
</dt> <dt>

[**IADsPrintQueueOperations**](/windows/desktop/api/Iads/nn-iads-iadsprintqueueoperations)
</dt> </dl>

 

 





