---
title: OnOffProgressValue enumeration
description: The types of power transitions Axe can track. It also specifies the type of tracing the OnOffHelper API provides.
ms.assetid: 2E0ACB05-9F10-4A16-B244-9766764D4F6A
keywords:
- OnOffProgressValue enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- OnOffProgressValue
api_location:
- AxeCore.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# OnOffProgressValue enumeration

The types of power transitions Axe can track. It also specifies the type of tracing the OnOffHelper API provides.

## Syntax


```C++
enum OnOffProgressValue {
  None                = 0, 
  NotifyOnly          = 0, 
  CancelNotification, 
  HybridBoot, 
  Boot, 
  Shutdown, 
  RebootCycle, 
  Standby, 
  Hibernate, 
  Max 

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

The assessment will be performing a power transition itself, but Axe does not need to do anything.

</dd> <dt>

<span id="NotifyOnly"></span><span id="notifyonly"></span><span id="NOTIFYONLY"></span>**NotifyOnly**
</dt> <dd>

The assessment will be performing a power transition itself, but Axe does not need to do anything.

</dd> <dt>

<span id="CancelNotification"></span><span id="cancelnotification"></span><span id="CANCELNOTIFICATION"></span>**CancelNotification**
</dt> <dd>

The assessment will not be performing the previously-reported power state transition.

</dd> <dt>

<span id="HybridBoot"></span><span id="hybridboot"></span><span id="HYBRIDBOOT"></span>**HybridBoot**
</dt> <dd>

The assessment will be rebooting the system using the HybridBoot technology.

</dd> <dt>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>**Boot**
</dt> <dd>

The assessment will be restarting the system using a full shutdown and restart.

</dd> <dt>

<span id="Shutdown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>**Shutdown**
</dt> <dd>

The assessment will shutdown the system. Tracing will only extend until the system powers off.

</dd> <dt>

<span id="RebootCycle"></span><span id="rebootcycle"></span><span id="REBOOTCYCLE"></span>**RebootCycle**
</dt> <dd>

The assessment is requesting tracing through both a shutdown and the subsequent start of the system.

</dd> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>**Standby**
</dt> <dd>

The assessment will be transitioning the system into Standby mode.

</dd> <dt>

<span id="Hibernate"></span><span id="hibernate"></span><span id="HIBERNATE"></span>**Hibernate**
</dt> <dd>

The assessment will be hibernating the system.

</dd> <dt>

<span id="Max"></span><span id="max"></span><span id="MAX"></span>**Max**
</dt> <dd>

An invalid transition type was reported. This enumerator is most often used for range checking the enumerator values. It should not be used to report an actual transition type. This is always the last enumerator.

</dd> </dl>

## Remarks

Before an assessment causes the system to power down or restart, it must notify Axe of the upcoming power state transition so that Axe ensures that the assessment will be restarted upon a user logging into the operating system again. Once a notification has been made, the assessment should send the **CancelNotification** enumerator if the assessment decides not to perform the transition that was previously reported so that Axe will not restart the assessment.

Managed code uses the [**OnOffProgressValue**](https://www.bing.com/search?q=**OnOffProgressValue**) enum.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



## See also

<dl> <dt>

[**ProgressType**](progresstype.md)
</dt> </dl>

 

 





