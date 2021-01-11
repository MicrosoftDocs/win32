---
description: Digit monitoring monitors the call for digits.
ms.assetid: 6ba28fdf-87d5-4d39-9e12-8201585a86ee
title: Digit Monitoring
ms.topic: article
ms.date: 05/31/2018
---

# Digit Monitoring

Digit monitoring monitors the call for digits. TAPI allows digits to be signaled according to two methods (digit modes):

-   Pulse Digits are signaled as pulse or rotary sequences. For detection, these pulses manifest themselves as nothing more than sequences of audible clicks. Valid pulse digits are '0' through '9'.
-   DTMF Digits are signaled as DTMF (Dual Tone Multiple Frequency) tones. Valid DTMF digits are '0' through '9', 'A'. 'B', 'C', 'D', '\*', and '\#'. Both the beginning and the down edge of DTMF digits can be monitored.

An application can enable or disable digit monitoring on a specified call with [**lineMonitorDigits**](/windows/desktop/api/Tapi/nf-tapi-linemonitordigits). When digit monitoring is enabled, detected digits cause the application to be notified with the [**LINE\_MONITORDIGITS**](line-monitordigits.md) message. This message provides the call handle on which the digit was detected as well as the digit value and the digit mode. The scope of digit monitoring is bound by the lifetime of the call. Digit monitoring on a call ends as soon as the call *disconnects* or goes *idle*.

 

 



