---
description: The following is an example message file that can be used to build a resource-only DLL to be used with the service sample when writing events to the event log.
ms.assetid: d0d46041-5608-4abf-b833-7aae1744ef60
title: Sample.mc
ms.topic: article
ms.date: 05/31/2018
---

# Sample.mc

The following is an example message file that can be used to build a resource-only DLL to be used with the service sample when writing events to the event log.

Use the following steps to build the DLL:

1.  **mc -U sample.mc**
2.  **rc -r sample.rc**
3.  **link -dll -noentry -out:sample.dll sample.res**

``` syntax
MessageIdTypedef=DWORD

SeverityNames=(Success=0x0:STATUS_SEVERITY_SUCCESS
    Informational=0x1:STATUS_SEVERITY_INFORMATIONAL
    Warning=0x2:STATUS_SEVERITY_WARNING
    Error=0x3:STATUS_SEVERITY_ERROR
    )


FacilityNames=(System=0x0:FACILITY_SYSTEM
    Runtime=0x2:FACILITY_RUNTIME
    Stubs=0x3:FACILITY_STUBS
    Io=0x4:FACILITY_IO_ERROR_CODE
)

LanguageNames=(English=0x409:MSG00409)

; // The following are message definitions.

MessageId=0x1
Severity=Error
Facility=Runtime
SymbolicName=SVC_ERROR
Language=English
An error has occurred (%2).
.

; // A message file must end with a period on its own line
; // followed by a blank line.
```

## Related topics

<dl> <dt>

[The Complete Service Sample](the-complete-service-sample.md)
</dt> </dl>

 

 



