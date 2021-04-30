---
title: /target switch
description: The /target switch enables the MIDL compiler to enable optimizations available only on recent versions of Windows. The /target switch automatically activates additional switches.
ms.assetid: 8c5aa319-e6a6-4803-99f3-ed8751d565d5
keywords:
- /target switch MIDL
topic_type:
- apiref
api_name:
- /target
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# /target switch

The **/target** switch enables the MIDL compiler to enable optimizations available only on recent versions of Windows. The **/target** switch automatically activates additional switches.

``` syntax
midl /target level
```

## Switch Options

<dl> <dt>

*level* 
</dt> <dd>

Specifies the target level, such as NT50, NT51, NT60, NT61, NT62, or NT100.

</dd> </dl>

## Remarks

The **/target** switch automatically activates additional switches, based on the operating system, as specified in the following table:



| Operating system | /target level | Switches Activated                     |
|------------------|---------------|----------------------------------------|
| Windows 2000     | NT50          | /Oicf /error all /robust               |
| Windows XP       | NT51          | /Oicf /error all /robust /protocol all |
| Windows Vista    | NT60          | /Oicf /error all /robust /protocol all |
| Windows 7        | NT61          | /Oicf /error all /robust /protocol all |
| Windows 8        | NT62          | /Oicf /error all /robust /protocol all |
| Windows 10       | NT100         | /Oicf /error all /robust /protocol all |
 

To ensure a stub runs on the system specified by the **/target** switch, MIDL issues an error when a feature available only on a more recent version of Windows is present. The following table specifies the minimum **/target** level required to enable the feature. Higher target levels include all features from lower target levels.



| Minimum required /target level | Features                                                                                                                                                                                          |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NT50                           | /robust<br/> \[message\]<br/> \[async\]<br/> \[async\_uuid\]<br/> \[notify\] in /Oicf mode<br/> \[encode\] or \[decode\] in /Oicf mode<br/>                   |
| NT51                           | /protocol 64-bit support<br/> \[partial\_ignore\]<br/> \[force\_allocate\]<br/>                                                                                                 |
| NT60                           | Forced complex structure marshalling<br/> Context handles in an array or structure<br/> \[range\] support for unsized strings<br/> \[type\_strict\_context\_handle\]<br/> |
| NT61                           | Direct COM stub calls for interfaces with less than 32 methods requires linking COM stubs with **OLE32.DLL**.<br/>                                                                          |
| NT62                           | ARM support<br/> WinRT support<br/>                                                                                                                                                   |
| NT100                          | \[system_handle\] support<br /> |


 

## Examples

**midl /target NT50**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> </dl>
