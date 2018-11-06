---
title: Producing a Dialog Box for Selecting a Filter
description: Producing a Dialog Box for Selecting a Filter
ms.assetid: 4cbb9276-6ce6-4cf4-a000-2b4f9ac42b31
keywords:
- audio compression manager (ACM),producing dialog boxes
- ACM (audio compression manager),producing dialog boxes
- ACM examples,producing dialog boxes
- producing dialog boxes
- acmFilterChoose function
- audio compression manager (ACM),selecting filters
- ACM (audio compression manager),selecting filters
- ACM examples,selecting filters
- selecting filters
ms.topic: article
ms.date: 05/31/2018
---

# Producing a Dialog Box for Selecting a Filter

An application can allow users to select an arbitrary filter operation and apply it to waveform-audio data. In the following example, the application allocates a buffer to hold the filter and then uses the [**acmFilterChoose**](/windows/desktop/api/Msacm/nf-msacm-acmfilterchoose) function to select the filter. The functions in this example must be called with the appropriate filter or filter tag.


```C++
MMRESULT        mmr; 
ACMFILTERCHOOSE afc; 
PWAVEFILTER     pwfltr; 
DWORD           cbwfltr; 
 
// Determine the maximum size required for any valid filter 
// for which the ACM has a driver installed and enabled. 
mmr = acmMetrics(NULL, ACM_METRIC_MAX_SIZE_FILTER, &cbwfltr); 
if (MMSYSERR_NOERROR != mmr) { 
 
    // The ACM probably has no drivers installed and 
    // enabled for filter operations. 
    return (mmr); 
} 
 
// Dynamically allocate a structure large enough to hold the 
// maximum sized filter enabled in the system. 
pwfltr = (PWAVEFILTER)LocalAlloc(LPTR, (UINT)cbwfltr); 
if (NULL == pwfltr) { 
    return (MMSYSERR_NOMEM); 
} 
 
// Initialize the ACMFILTERCHOOSE members. 
memset(&afc, 0, sizeof(afc)); 
 
afc.cbStruct    = sizeof(afc); 
afc.fdwStyle    = 0L;               // no special style flags 
afc.hwndOwner   = hwnd;             // hwnd of parent window 
afc.pwfltr      = pwfltr;           // wfltr to receive selection 
afc.cbwfltr     = cbwfltr;          // size of wfltr buffer 
afc.pszTitle    = TEXT("Any Filter Selection"); 
 
// Call the ACM to bring up the filter-selection dialog box. 
mmr = acmFilterChoose(&afc); 
if (MMSYSERR_NOERROR == mmr) { 
    // The user selected a valid filter. The pwfltr buffer, 
    // allocated above, contains the complete filter description. 
} 
 
// Clean up and exit. 
LocalFree((HLOCAL)pwfltr); 
return (mmr); 
 
```



 

 




