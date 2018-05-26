---
Description: Most counter types use a formula for calculating a displayable value for the counter.
ms.assetid: b65a6874-fffb-41af-8620-27d4036cc7b2
title: Calculating Counter Values
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Calculating Counter Values

Most counter types use a formula for calculating a displayable value for the counter. For a list of counter types and their formulas, see the Counter Types section of the [Windows Server 2003 Deployment Kit](Http://go.microsoft.com/fwlink/p/?linkid=84422). If the counter requires two samples in order to calculate the displayable value, the counter type's **PERF\_DELTA\_COUNTER** flag is set.

The following example shows how to use the raw data to calculate a displayable value for each counter type. This example builds on the example in [Retrieving Counter Data](retrieving-counter-data.md).


```C++
// Use the CounterType to determine how to calculate the displayable
// value. The case statement includes the formula used to calculate 
// the value.
BOOL DisplayCalculatedValue(RAW_DATA* pSample1, RAW_DATA* pSample2)
{
    BOOL fSuccess = TRUE;
    ULONGLONG numerator = 0;
    LONGLONG denominator = 0;
    double DisplayValue = 0;
    DWORD DisplayValue2 = 0;

    // If the counter type contains the PERF_DELTA_COUNTER flag, you need
    // two samples to calculate the value. 
    if (PERF_DELTA_COUNTER == (pSample1->CounterType & PERF_DELTA_COUNTER) &amp;&amp;
        NULL == pSample2)
    {
        wprintf(L"The counter type requires two samples but only one sample was passed.\n");
        fSuccess = FALSE;
        goto cleanup;
    }
    
    // Check for integer overflow or bad data from provider (the data from 
    // sample 2 must be greater than the data from sample 1).
    if (pSample2 != NULL &amp;&amp; pSample1->Data > pSample2->Data)
    {                     
        // You would probably just drop the older sample and continue.                
        wprintf(L"Sample1 (%I64u) is larger than sample2 (%I64u).\n", pSample1->Data, pSample2->Data);
        fSuccess = FALSE;
        goto cleanup;
    }

    switch (pSample1->CounterType) 
    {
        case PERF_COUNTER_COUNTER:  //(N1 - N0)/((D1 - D0)/F)
        case PERF_SAMPLE_COUNTER:
        case PERF_COUNTER_BULK_COUNT:  
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue2 = (DWORD)(numerator/((double)denominator/pSample2->Frequency));
            wprintf(L"Display value is %u%s\n", DisplayValue2,
            (pSample1->CounterType == PERF_SAMPLE_COUNTER) ? L"." : L"/sec.");
            break;

        case PERF_COUNTER_QUEUELEN_TYPE:  //(N1 - N0)/(D1 - D0)
        case PERF_COUNTER_100NS_QUEUELEN_TYPE:  
        case PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE:
        case PERF_COUNTER_LARGE_QUEUELEN_TYPE:  
        case PERF_AVERAGE_BULK:  //don't display
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = (double)numerator/denominator;
            if (pSample1->CounterType != PERF_AVERAGE_BULK)
                wprintf(L"Display value is %f.\n", DisplayValue);
            break;

        case PERF_OBJ_TIME_TIMER:  // 100*(N1 - N0)/(D1 - D0)
        case PERF_COUNTER_TIMER:  
        case PERF_100NSEC_TIMER:
        case PERF_PRECISION_SYSTEM_TIMER: 
        case PERF_PRECISION_100NS_TIMER:
        case PERF_PRECISION_OBJECT_TIMER:
        case PERF_SAMPLE_FRACTION:  // 100*(N1 - N0)/(B1 - B0)
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = (double)(100*numerator)/denominator;
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_COUNTER_TIMER_INV:  // 100*(1- ((N1 - N0)/(D1 - D0)))
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = 100*(1 - ((double)numerator/denominator));
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_100NSEC_TIMER_INV:  // 100*(1- (N1 - N0)/(D1 - D0))
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = 100*(1 - (double)numerator/denominator);
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_COUNTER_MULTI_TIMER:  // 100*((N1 - N0)/((D1 - D0)/TB))/B1
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            denominator /= pSample2->Frequency;
            DisplayValue = 100*((double)numerator/denominator)/pSample2->MultiCounterData;
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_100NSEC_MULTI_TIMER:  // 100*((N1 - N0)/(D1 - D0))/B1
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = 100*((double)numerator/denominator)/pSample2->MultiCounterData;
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_COUNTER_MULTI_TIMER_INV:  // 100*(B1- ((N1 - N0)/(D1 - D0)))
        case PERF_100NSEC_MULTI_TIMER_INV:
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = 100*(pSample2->MultiCounterData - ((double)numerator/denominator));
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_COUNTER_RAWCOUNT:  // N as decimal
        case PERF_COUNTER_LARGE_RAWCOUNT:
            wprintf(L"Display value is %I64u.\n", pSample1->Data);
            break;

        case PERF_COUNTER_RAWCOUNT_HEX:  // N as hexadecimal
        case PERF_COUNTER_LARGE_RAWCOUNT_HEX:
            wprintf(L"Display value is %I64x.\n", pSample1->Data);
            break;

        case PERF_COUNTER_DELTA:  // N1 - N0
        case PERF_COUNTER_LARGE_DELTA:
            DisplayValue = (double)(pSample2->Data - pSample1->Data);
            wprintf(L"Display value is %I64u.\n", DisplayValue);
            break;

        case PERF_RAW_FRACTION:  // 100*N/B
        case PERF_LARGE_RAW_FRACTION:
            DisplayValue = (double)100*pSample1->Data/pSample1->Time;
            wprintf(L"Display value is %f%%.\n", DisplayValue);
            break;

        case PERF_AVERAGE_TIMER:  // ((N1 - N0)/TB)/(B1 - B0)
            numerator = pSample2->Data - pSample1->Data;
            denominator = pSample2->Time - pSample1->Time;
            DisplayValue = (double)numerator/pSample2->Frequency/denominator;
            wprintf(L"Display value is %f in seconds.\n", DisplayValue);
            break;

        case PERF_ELAPSED_TIME:  //(D0 - N0)/F
            DisplayValue = (double)(pSample1->Time - pSample1->Data)/pSample1->Frequency;
            wprintf(L"Display value is %f in seconds.\n", DisplayValue);
            break;

        default:
            wprintf(L"Counter type not found.\n");
            fSuccess = FALSE;
            break;
    }

cleanup:

    return fSuccess;
}
```



 

 



