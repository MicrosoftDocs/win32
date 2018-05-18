---
title: ProgressIdleValue enumeration
description: Specifies the type of Idle progress type that has occurred.
ms.assetid: 'C1339942-9F02-4A89-9F19-7DF94933C8DC'
keywords: ["ProgressIdleValue enumeration Access Execution Engine"]
topic_type:
- apiref
api_name:
- ProgressIdleValue
api_location:
- AxeCore.h
api_type:
- HeaderDef
---

# ProgressIdleValue enumeration

Specifies the type of Idle progress type that has occurred.

## Syntax


```C++
enum ProgressIdleValue {
  ProgressIdleValueNone                   = 0, 
  ProgressIdleValueBegin, 
  ProgressIdleValueEnd, 
  ProgressIdleValueEnterConnectedStandby, 
  ProgressIdleValueMax 

};
```



## Constants

<dl> <dt>

<span id="ProgressIdleValueNone"></span><span id="progressidlevaluenone"></span><span id="PROGRESSIDLEVALUENONE"></span>**ProgressIdleValueNone**
</dt> <dd>

No idle progress is being reported. This enumerator should never occur at runtime.

</dd> <dt>

<span id="ProgressIdleValueBegin"></span><span id="progressidlevaluebegin"></span><span id="PROGRESSIDLEVALUEBEGIN"></span>**ProgressIdleValueBegin**
</dt> <dd>

The assessment is beginning an idle period.

</dd> <dt>

<span id="ProgressIdleValueEnd"></span><span id="progressidlevalueend"></span><span id="PROGRESSIDLEVALUEEND"></span>**ProgressIdleValueEnd**
</dt> <dd>

The assessment is ending an idle period.

</dd> <dt>

<span id="ProgressIdleValueEnterConnectedStandby"></span><span id="progressidlevalueenterconnectedstandby"></span><span id="PROGRESSIDLEVALUEENTERCONNECTEDSTANDBY"></span>**ProgressIdleValueEnterConnectedStandby**
</dt> <dd>

The assessment is beginning a connected standby idle period.

</dd> <dt>

<span id="ProgressIdleValueMax"></span><span id="progressidlevaluemax"></span><span id="PROGRESSIDLEVALUEMAX"></span>**ProgressIdleValueMax**
</dt> <dd>

An invalid idle value was reported. This enumerator is most often used for range checking the enumerator values. It should not be used to report an actual idle value.

</dd> </dl>

## Remarks

When measuring the energy efficiency of a system, both active and idle periods must be analyzed. The **ProgressTypeIdle** progress enumerator is used by workloads running under the Energy Efficiency assessment to mark where the idle periods appear in the traces that are being gathered. This enables analysis after the Energy Efficiency assessment has completed.

Managed code uses the [**ProgressIdleValue**](axe-progressidlevalue_om) enum.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



## See also

<dl> <dt>

[**ProgressType**](progresstype.md)
</dt> </dl>

 

 





