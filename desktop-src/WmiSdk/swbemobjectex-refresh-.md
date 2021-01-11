---
description: Updates the data for objects that have data supplied by a performance provider, such as the Performance Counter Classes. You can obtain updated data more quickly and without a call to SWbemServices.Get\_.
ms.assetid: 6aeaa336-fb98-4eda-b746-fc958198d8ae
ms.tgt_platform: multiple
title: SWbemObjectEx.Refresh_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectEx.Refresh_
- ISWbemObjectEx.Refresh_
- ISWbemObjectEx.Refresh_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectEx.Refresh\_ method

The **Refresh\_** method of [**SWbemObjectEx**](swbemobjectex.md) updates the data for objects that have data supplied by a performance provider, such as the [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes). You can obtain updated data more quickly and without a call to [**SWbemServices.Get\_**](swbemservices-get.md).

For more information about this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemObjectEx.Refresh_( _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved operation flags which, if specified, must be 0 (zero).

</dd> <dt>

*objWbemNamedValueSet* \[in, optional\]
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that sets context for the operation.

</dd> </dl>

## Return value

This method does not return a value.

## Error codes

After completion of the **Refresh\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

The provider failed internally, even though the operation was valid.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The requested format was not found.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

One of the parameters to the call is not correct.

</dd> <dt>

**wbemErrRefresherBusy** - 2147749975 (0x80041057)
</dt> <dd>

The refresher is busy with another operation.

</dd> <dt>

**wbemPartialResults** - 2147745808 (0x80040010)
</dt> <dd>

Not all of the objects, enumerators, or nested refreshers were successfully updated. This return is not an error but an indication that the operation was incomplete.

</dd> </dl>

## Examples

The following script code example shows how to obtain both raw and cooked performance counters for the system process. The objects are refreshed every two seconds and the properties displayed.


```VB
' Get the performance counter instance for the System process
set PerfRaw = GetObject( _
    "winmgmts:win32_perfrawdata_perfproc_process.name='system'")
set PerfCooked = GetObject( _
    "winmgmts:win32_perfformatteddata_perfproc_process.name='system'")

' Display some properties in a loop
for I = 1 to 5
    Wscript.Echo "HandleCount = "& PerfRaw.HandleCount & _
         " Raw ThreadCount = " & PerfRaw.ThreadCount & _
        " Cooked ThreadCount = " & PerfCooked.ThreadCount
    
    Wscript.Sleep 2000
    
' Refresh the objects
    PerfRaw.Refresh_
    PerfCooked.Refresh_
next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectEx<br/>                                                         |
| IID<br/>                      | IID\_ISWbemObjectEx<br/>                                                          |



## See also

<dl> <dt>

[**SWbemObjectEx**](swbemobjectex.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

