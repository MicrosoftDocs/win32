---
description: Runs an experiment.
MS-HAID: vspixengine.IPixEngine\_RunExperiment\_Experiment\_IRunExperimentCallback\_ptr\_INewFramesCallback\_ptr\_IFileIOCallback\_ptr\_DWORD\_ExperimentTrigger\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine::RunExperiment method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: A2EEC278-C074-44B3-94DC-E2D9DC770576
api_name: 
 - IPixEngine.RunExperiment
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine_runexperiment_experiment_irunexperimentcallback_ptr_inewframescallback_ptr_ifileiocallback_ptr_dword_experimenttrigger_arr"></span>IPixEngine::RunExperiment method

Runs an experiment.

## Syntax


```C++
HRESULT RunExperiment(
   Experiment               experiment,
   IRunExperimentCallback * pRequestCallback,
   INewFramesCallback*      callbacks,
   IFileIOCallback*         pFileIOCallback,
   DWORD                    triggersCount,
   ExperimentTrigger []     count4_triggersBuffer
);
```

## Parameters

*experiment*   
Describes the experiment to be run.

*pRequestCallback*   
The address of a function used to notify the host that engine has started the experiment.

*callbacks*   
The address of a function used to notify the host that new frames have been captured.

*pFileIOCallback*   
The address of a function used to notify the host of file IO errors during parsing.

*triggersCount*   
The number of triggers in the experiment.

*count4\_triggersBuffer*   
Capture triggers.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine**](/windows/desktop/direct3dtools/ipixengine)

 

 
