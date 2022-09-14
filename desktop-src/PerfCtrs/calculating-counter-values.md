---
description: Most counter types use a formula for calculating a displayable value for the counter.
ms.assetid: b65a6874-fffb-41af-8620-27d4036cc7b2
title: Calculating Counter Values
ms.topic: article
ms.date: 08/17/2020
---

# Calculating Counter Values

Most counter types use a formula for calculating a displayable value for the counter. For a list of counter types and their formulas, see the Counter Types section of the [Windows Server 2003 Deployment Kit](/previous-versions/windows/it-pro/windows-server-2003/cc776490(v=ws.10)). If the counter requires two samples in order to calculate the displayable value, the counter type's `PERF_DELTA_COUNTER` flag is set.

The following example shows how to use the raw data to calculate a displayable value for each counter type. This example builds on the example in [Retrieving Counter Data](retrieving-counter-data.md).

```C
// Contains the elements required to calculate a counter value.
typedef struct
{
    DWORD CounterType;
    DWORD MultiCounterData;  // Second raw counter value for multi-valued counters
    ULONGLONG Data;          // Raw counter data
    LONGLONG Time;           // Is a time value or a base value
    LONGLONG Frequency;
} RAW_DATA;

// Use the CounterType to determine how to calculate the displayable
// value. The case statement includes the formula used to calculate
// the value.
BOOL DisplayCalculatedValue(RAW_DATA* pSample0, RAW_DATA* pSample1)
{
    BOOL fSuccess = TRUE;
    ULONGLONG numerator = 0;
    LONGLONG denominator = 0;
    double doubleValue = 0;
    DWORD dwordValue = 0;

    if (NULL == pSample1)
    {
        // Return error if the counter type requires two samples to calculate the value.
        switch (pSample0->CounterType)
        {
        default:
            if (PERF_DELTA_COUNTER != (pSample0->CounterType & PERF_DELTA_COUNTER))
            {
                break;
            }
            __fallthrough;
        case PERF_AVERAGE_TIMER: // Special case.
        case PERF_AVERAGE_BULK:  // Special case.
            wprintf(L"The counter type requires two samples but only one sample was provided.\n");
            fSuccess = FALSE;
            goto cleanup;
        }
    }
    else
    {
        if (pSample0->CounterType != pSample1->CounterType)
        {
            wprintf(L"The samples have inconsistent counter types.\n");
            fSuccess = FALSE;
            goto cleanup;
        }

        // Check for integer overflow or bad data from provider (the data from
        // sample 2 must be greater than the data from sample 1).
        if (pSample0->Data > pSample1->Data)
        {
            // Can happen for various reasons. Commonly occurs with the Process counterset when
            // multiple processes have the same name and one of them starts or stops.
            // Normally you'll just drop the older sample and continue.
            wprintf(L"Sample0 (%llu) is larger than sample1 (%llu).\n", pSample0->Data, pSample1->Data);
            fSuccess = FALSE;
            goto cleanup;
        }
    }

    switch (pSample0->CounterType)
    {
    case PERF_COUNTER_COUNTER:
    case PERF_SAMPLE_COUNTER:
    case PERF_COUNTER_BULK_COUNT:
        // (N1 - N0) / ((D1 - D0) / F)
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        dwordValue = (DWORD)(numerator / ((double)denominator / pSample1->Frequency));
        wprintf(L"Display value is: %lu%ls\n", dwordValue,
            (pSample0->CounterType == PERF_SAMPLE_COUNTER) ? L"" : L"/sec");
        break;

    case PERF_COUNTER_QUEUELEN_TYPE:
    case PERF_COUNTER_100NS_QUEUELEN_TYPE:
    case PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE:
    case PERF_COUNTER_LARGE_QUEUELEN_TYPE:
    case PERF_AVERAGE_BULK:  // normally not displayed
        // (N1 - N0) / (D1 - D0)
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = (double)numerator / denominator;
        if (pSample0->CounterType != PERF_AVERAGE_BULK)
            wprintf(L"Display value is: %f\n", doubleValue);
        break;

    case PERF_OBJ_TIME_TIMER:
    case PERF_COUNTER_TIMER:
    case PERF_100NSEC_TIMER:
    case PERF_PRECISION_SYSTEM_TIMER:
    case PERF_PRECISION_100NS_TIMER:
    case PERF_PRECISION_OBJECT_TIMER:
    case PERF_SAMPLE_FRACTION:
        // 100 * (N1 - N0) / (D1 - D0)
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = (double)(100 * numerator) / denominator;
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_COUNTER_TIMER_INV:
        // 100 * (1 - ((N1 - N0) / (D1 - D0)))
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = 100 * (1 - ((double)numerator / denominator));
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_100NSEC_TIMER_INV:
        // 100 * (1- (N1 - N0) / (D1 - D0))
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = 100 * (1 - (double)numerator / denominator);
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_COUNTER_MULTI_TIMER:
        // 100 * ((N1 - N0) / ((D1 - D0) / TB)) / B1
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        denominator /= pSample1->Frequency;
        doubleValue = 100 * ((double)numerator / denominator) / pSample1->MultiCounterData;
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_100NSEC_MULTI_TIMER:
        // 100 * ((N1 - N0) / (D1 - D0)) / B1
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = 100 * ((double)numerator / denominator) / pSample1->MultiCounterData;
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_COUNTER_MULTI_TIMER_INV:
    case PERF_100NSEC_MULTI_TIMER_INV:
        // 100 * (B1 - ((N1 - N0) / (D1 - D0)))
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = 100 * (pSample1->MultiCounterData - ((double)numerator / denominator));
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_COUNTER_RAWCOUNT:
    case PERF_COUNTER_LARGE_RAWCOUNT:
        // N as decimal
        wprintf(L"Display value is: %llu\n", pSample0->Data);
        break;

    case PERF_COUNTER_RAWCOUNT_HEX:
    case PERF_COUNTER_LARGE_RAWCOUNT_HEX:
        // N as hexadecimal
        wprintf(L"Display value is: 0x%llx\n", pSample0->Data);
        break;

    case PERF_COUNTER_DELTA:
    case PERF_COUNTER_LARGE_DELTA:
        // N1 - N0
        wprintf(L"Display value is: %llu\n", pSample1->Data - pSample0->Data);
        break;

    case PERF_RAW_FRACTION:
    case PERF_LARGE_RAW_FRACTION:
        // 100 * N / B
        doubleValue = (double)100 * pSample0->Data / pSample0->Time;
        wprintf(L"Display value is: %f%%\n", doubleValue);
        break;

    case PERF_AVERAGE_TIMER:
        // ((N1 - N0) / TB) / (B1 - B0)
        numerator = pSample1->Data - pSample0->Data;
        denominator = pSample1->Time - pSample0->Time;
        doubleValue = (double)numerator / pSample1->Frequency / denominator;
        wprintf(L"Display value is: %f seconds\n", doubleValue);
        break;

    case PERF_ELAPSED_TIME:
        // (D0 - N0) / F
        doubleValue = (double)(pSample0->Time - pSample0->Data) / pSample0->Frequency;
        wprintf(L"Display value is: %f seconds\n", doubleValue);
        break;

    case PERF_COUNTER_TEXT:
    case PERF_SAMPLE_BASE:
    case PERF_AVERAGE_BASE:
    case PERF_COUNTER_MULTI_BASE:
    case PERF_RAW_BASE:
    case PERF_COUNTER_NODATA:
    case PERF_PRECISION_TIMESTAMP:
        wprintf(L"Non-printing counter type.\n");
        break;

    default:
        wprintf(L"Unrecognized counter type.\n");
        fSuccess = FALSE;
        break;
    }

cleanup:

    return fSuccess;
}
```
