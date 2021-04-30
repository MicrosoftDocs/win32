---
description: The processor performance control policy constants indicate the processor performance control algorithm applied to a power scheme.
ms.assetid: 928ba485-f767-47df-8b57-7630c68068a7
title: Processor Performance Control Policy Constants (WinNT.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Processor Performance Control Policy Constants

The processor performance control policy constants indicate the processor performance control algorithm applied to a power scheme.



| Constant/value                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PO_THROTTLE_ADAPTIVE"></span><span id="po_throttle_adaptive"></span><dl> <dt>**PO\_THROTTLE\_ADAPTIVE**</dt> <dt>3</dt> </dl> | Attempts to match the performance of the processor to the current demand. This policy will use both high and low voltage and frequency states. This policy will lower the performance of the processor to the lowest voltage available whenever there is insufficient demand to justify a higher voltage. This policy will engage processor clock throttling if the C3 state is not being utilized, and in response to thermal events.<br/> |
| <span id="PO_THROTTLE_CONSTANT"></span><span id="po_throttle_constant"></span><dl> <dt>**PO\_THROTTLE\_CONSTANT**</dt> <dt>1</dt> </dl> | Does not allow the processor to use any high voltage performance states. This policy will not engage processor clock throttling, except in response to thermal events.<br/>                                                                                                                                                                                                                                                                 |
| <span id="PO_THROTTLE_DEGRADE"></span><span id="po_throttle_degrade"></span><dl> <dt>**PO\_THROTTLE\_DEGRADE**</dt> <dt>2</dt> </dl>    | Does not allow the processor to use any high voltage performance states. This policy will engage processor clock throttling when the battery is below a certain threshold, if the C3 state is not being utilized, or in response to thermal events.<br/>                                                                                                                                                                                    |
| <span id="PO_THROTTLE_NONE"></span><span id="po_throttle_none"></span><dl> <dt>**PO\_THROTTLE\_NONE**</dt> <dt>0</dt> </dl>             | No processor performance control is applied. This policy always runs the processor at its highest possible performance level. This policy will not engage processor clock throttling, except in response to thermal events.<br/>                                                                                                                                                                                                            |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>WinNT.h (include Windows.h)</dt> </dl> |



 

 




