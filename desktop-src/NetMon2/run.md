---
description: The expert must implement the Run function. Network Monitor calls the Run function to start the expert within the expert DLL.
ms.assetid: 9ef3941b-d9e9-4acb-97ed-5f39573f2946
title: Run callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Run
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# Run callback function

The expert must implement the **Run** function. Network Monitor calls the **Run** function to start the expert within the expert DLL.

## Syntax


```C++
BOOL WINAPI Run(
  _In_ HEXPERTKEY         hExpertKey,
  _In_ PEXPERTCONFIG      pConfig,
  _In_ PEXPERTSTARTUPINFO pExpertStartupInfo,
  _In_ DWORD              StartupFlags,
  _In_ HWND               hWndParent
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique identifier of the expert that is passed back to all expert-specific Network Monitor functions.

> [!Note]  
> The *hExpertKey* identifier may pass an expert key that is different from the expert key that the [**Configure**](configure.md) function passes.

 

</dd> <dt>

*pConfig* \[in\]
</dt> <dd>

Pointer to the existing configuration. The *pConfig* parameter may be **NULL** which means that the expert can run with hard-coded defaults, or startup information that the *pExpertStartupInfo* parameter references.

</dd> <dt>

*pExpertStartupInfo* \[in\]
</dt> <dd>

Pointer to the capture element that has focus when the expert starts.

</dd> <dt>

*StartupFlags* \[in\]
</dt> <dd>

Indicator for how the expert should use the *pExpertStartupInfo* parameter.

The only flag defined is:



| Value                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EXPERT_STARTUP_FLAG_USE_STARTUP_DATA_OVER_CONFIG_DATA."></span><span id="expert_startup_flag_use_startup_data_over_config_data."></span><dl> <dt>**EXPERT\_STARTUP\_FLAG\_USE\_STARTUP\_DATA\_OVER\_CONFIG\_DATA.**</dt> </dl> | This flag indicates that the expert uses the *pExpertStartupInfo* parameter, and does not use the *pConfig* parameter. Typically, you can set this flag when the expert can start from a right-mouse click. If the flag is not set, the following two things can occur: either the expert does not start from a right-mouse click, or the expert starts from a right-mouse click, and then the user configures it.<br/> |



 

</dd> <dt>

*hWndParent* \[in\]
</dt> <dd>

The *hWnd* parameter of the parent (usually the Network Monitor user interface).

</dd> </dl>

## Return value

If the function is successful (that is, if the expert starts), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

When running, the expert loops through the frames in the capture file and either generates a report or creates events that show problems.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




