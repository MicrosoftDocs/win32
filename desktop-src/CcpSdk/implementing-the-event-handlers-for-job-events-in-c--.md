---
Description: 'When you subscribe to job events, you must implement a class that derives from ISchedulerJobEvents.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c5752f3d-e610-4b96-a96e-324096e43869'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Implementing the Event Handlers for Job Events in C++
---

# Implementing the Event Handlers for Job Events in C++

When you subscribe to job events, you must implement a class that derives from [**ISchedulerJobEvents**](ischedulerjobevents.md). The following C++ example shows a class that implements the [**ISchedulerJobEvents**](ischedulerjobevents.md) interface. For an example that shows how to subscribe to the events, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).


```C++
extern HANDLE g_JobDoneEvent; // Defined in the "Creating and Submitting a Job" topic's C++ example

// Dispath IDs that identify the methods for the ISchedulerJobEvents interface.
#define DISPID_0NJOBSTATE    0x60020000
#define DISPID_ONTASKSTATE   0x60020001

class CJobEventHandler : public ISchedulerJobEvents
{
    LONG m_lRefCount;
    ITypeInfo* m_pTypeInfo;

public:
    // Constructor, Destructor
    CJobEventHandler()
    {
        m_lRefCount = 1;
        m_pTypeInfo = NULL;
    };

    ~CJobEventHandler()
    {
        if (m_pTypeInfo)
        {
            m_pTypeInfo->Release();
            m_pTypeInfo = NULL;
        }
    };

    // IUnknown methods
    HRESULT __stdcall QueryInterface(REFIID riid, LPVOID *ppvObj);
    ULONG __stdcall AddRef();
    ULONG __stdcall Release();

    // IDispatch methods
    HRESULT __stdcall GetTypeInfoCount(UINT* pCount);
    HRESULT __stdcall GetTypeInfo(UINT uiTInfoRequest, LCID lcid, ITypeInfo** ppTInfo);
    HRESULT __stdcall GetIDsOfNames(REFIID riid, OLECHAR** ppNames, UINT cNames, LCID lcid, DISPID* pDispId);
    HRESULT __stdcall Invoke(DISPID dispidMember, REFIID riid, LCID lcid, WORD wFlags,
        DISPPARAMS* pDispParams, VARIANT* pvarResult, EXCEPINFO* pExcepInfo, UINT* puArgErr);

    // ISchedulerJobEvents methods
    void __stdcall OnJobState(VARIANT sender, IJobStateEventArg* args);
    void __stdcall OnTaskState(VARIANT sender, ITaskStateEventArg* args);

private:

    HRESULT LoadTypeInfo(void);
    LPWSTR GetJobStateString(JobState state);
    LPWSTR GetTaskStateString(TaskState state);
};
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>// Strings associated with the job state values.
LPWSTR JobStateStrings[] = {
    L&quot;Configuring&quot;, L&quot;Submitted&quot;, L&quot;Validating&quot;, 
    L&quot;External validation&quot;, L&quot;Queued&quot;, L&quot;Running&quot;,
    L&quot;Finishing&quot;, L&quot;Finished&quot;, L&quot;Failed&quot;,
    L&quot;Canceled&quot;, L&quot;Canceling&quot; 
    };

// Strings associated with the task state values.
LPWSTR TaskStateStrings[] = {
    L&quot;Configuring&quot;, L&quot;Submitted&quot;, L&quot;Validating&quot;, 
    L&quot;Queued&quot;, L&quot;Dispatching&quot;, L&quot;Running&quot;,
    L&quot;Finishing&quot;, L&quot;Finished&quot;, L&quot;Failed&quot;,
    L&quot;Canceled&quot;, L&quot;Canceling&quot; 
    };


// IUnknown methods implementation.

HRESULT CJobEventHandler::QueryInterface(REFIID riid, LPVOID* ppvObj) 
{
    if (riid == __uuidof(IUnknown) || 
        riid == __uuidof(IDispatch) ||
        riid == __uuidof(ISchedulerJobEvents)) 
    {
        *ppvObj = this;
    }
    else
    {
        *ppvObj = NULL;
        return E_NOINTERFACE;
    }

    AddRef();
    return NOERROR;
}

ULONG CJobEventHandler::AddRef() 
{
    return InterlockedIncrement(&amp;m_lRefCount);
}

ULONG CJobEventHandler::Release() 
{
    ULONG  ulCount = InterlockedDecrement(&amp;m_lRefCount);

    if(0 == ulCount) 
    {
        delete this;
    }

    return ulCount;
}


// IDispatch methods implementation.

HRESULT __stdcall CJobEventHandler::GetTypeInfoCount(UINT* pctInfo)
{
    HRESULT hr = S_OK;

    if (pctInfo == NULL) 
        return E_INVALIDARG;

    hr = LoadTypeInfo();

    if (SUCCEEDED(hr))
        *pctInfo = 1;

    return hr;
}

HRESULT __stdcall CJobEventHandler::GetTypeInfo(UINT itInfo, LCID lcid, ITypeInfo** ppTInfo)
{
    HRESULT hr = S_OK;

    if (ppTInfo == NULL)
        return E_POINTER;

    if(itInfo != 0)
        return DISP_E_BADINDEX;

    *ppTInfo = NULL;

    hr = LoadTypeInfo();

    if (SUCCEEDED(hr))
    {
        m_pTypeInfo-&gt;AddRef();
        *ppTInfo = m_pTypeInfo;
    }

    return hr;
}

HRESULT __stdcall CJobEventHandler::GetIDsOfNames(REFIID riid, OLECHAR** rgszNames, UINT cNames, LCID lcid, DISPID* rgDispId)
{
    HRESULT hr = S_OK;

    hr = LoadTypeInfo();

    if (FAILED(hr))
        return hr;

    return (m_pTypeInfo-&gt;GetIDsOfNames(rgszNames, cNames, rgDispId));
}

// Invoke the event handler methods directly.
HRESULT __stdcall CJobEventHandler::Invoke(DISPID dispId, REFIID riid, LCID lcid, WORD wFlags,
    DISPPARAMS* pDispParams, VARIANT* pvarResult, EXCEPINFO* pExcepInfo, UINT* puArgErr)
{
    HRESULT hr = S_OK;
    ITaskStateEventArg* pTaskStateArgs = NULL;
    IJobStateEventArg* pJobStateArgs = NULL;
    _variant_t vSender;  
    _variant_t vArgs;


    if (2 != pDispParams-&gt;cArgs) 
        return E_INVALIDARG;

    vSender = pDispParams-&gt;rgvarg[1];  // IScheduler
    vArgs = pDispParams-&gt;rgvarg[0];    // Arguments 

    switch (dispId)
    {
        case DISPID_ONTASKSTATE :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_ITaskStateEventArg, (void**)&amp;pTaskStateArgs);
            if (SUCCEEDED(hr))
            {
                OnTaskState(vSender, pTaskStateArgs);
                pTaskStateArgs-&gt;Release();
                pTaskStateArgs = NULL;
            }
            break;

        case DISPID_0NJOBSTATE :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_IJobStateEventArg, (void**)&amp;pJobStateArgs);
            if (SUCCEEDED(hr))
            {
                OnJobState(vSender, pJobStateArgs);
                pJobStateArgs-&gt;Release();
                pJobStateArgs = NULL;
            }
            break;

        default:
            hr = DISP_E_BADINDEX;  // Bad dispId
    }

    return hr;
}


HRESULT CJobEventHandler::LoadTypeInfo(void)
{
    HRESULT hr;
    ITypeLib* pTypeLib = NULL;

    if (m_pTypeInfo)
        return S_OK;

    // Load type library.
    hr = LoadRegTypeLib(LIBID_Microsoft_Hpc_Scheduler, 2, 0, LOCALE_USER_DEFAULT, &amp;pTypeLib);

    if (SUCCEEDED(hr))
    {
        // Get type information for interface of the object.
        hr = pTypeLib-&gt;GetTypeInfoOfGuid(DIID_ISchedulerJobEvents, &amp;m_pTypeInfo);
        pTypeLib-&gt;Release();

        if (FAILED(hr))
            m_pTypeInfo = NULL;
    }

    return hr;
}


// ISchedulerJobEvents implementation

// The SchedulerJob object will call both handler methods. If you do not want
// to handle the event, simply return.

void CJobEventHandler::OnJobState(VARIANT sender, IJobStateEventArg* pargs)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    ISchedulerJob* pJob = NULL;
    JobState State;
    long JobId = 0;

    hr = pargs-&gt;get_NewState(&amp;State);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    hr = pargs-&gt;get_JobId(&amp;JobId);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    wprintf(L&quot;\nOnJobState: State for job %d is %s\n&quot;, JobId, GetJobStateString(State));

    hr = sender.pdispVal-&gt;QueryInterface(__uuidof(IScheduler), reinterpret_cast&lt;void **&gt; (&amp;pScheduler));

    hr = pScheduler-&gt;OpenJob(JobId, &amp;pJob);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    // TODO: Do something with the job.

    if (JobState_Finished == State ||
        JobState_Failed == State ||
        JobState_Canceled == State)
    {
        SetEvent(g_JobDoneEvent);
    }

cleanup:

    if (pScheduler)
        pScheduler-&gt;Release();

    if (pJob)
        pJob-&gt;Release();
}


void CJobEventHandler::OnTaskState(VARIANT sender, ITaskStateEventArg* pargs)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;
    ITaskId* pTaskId = NULL;
    TaskState State;
    BSTR bstr = NULL;
    long JobId = 0;
    long JobTaskId = 0;
    long InstanceId = 0;

    hr = pargs-&gt;get_NewState(&amp;State);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    hr = pargs-&gt;get_JobId(&amp;JobId);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    hr = pargs-&gt;get_TaskId(&amp;pTaskId);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    hr = pTaskId-&gt;get_JobTaskId(&amp;JobTaskId);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    hr = pTaskId-&gt;get_InstanceId(&amp;InstanceId);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    if (InstanceId)
        wprintf(L&quot;\nOnTaskState: State for instance %d of task %d is %s\n&quot;, 
            InstanceId, JobTaskId, GetTaskStateString(State));
    else
        wprintf(L&quot;\nOnTaskState: State for task %d is %s\n&quot;, JobTaskId, GetTaskStateString(State));

    hr = sender.pdispVal-&gt;QueryInterface(__uuidof(IScheduler), reinterpret_cast&lt;void **&gt; (&amp;pScheduler));

    // If the task is finished or failed, get the output.
    if (TaskState_Finished == State || TaskState_Failed == State)
    {
        hr = pScheduler-&gt;OpenJob(JobId, &amp;pJob);
        if (FAILED(hr))
        {
            // Handle error;
            goto cleanup;
        }

        hr = pJob-&gt;OpenTask(pTaskId, &amp;pTask);
        if (FAILED(hr))
        {
            // Handle error;
            goto cleanup;
        }

        hr = pTask-&gt;get_Output(&amp;bstr);
        if (FAILED(hr))
        {
            // Handle error;
            goto cleanup;
        }

        wprintf(L&quot;Output from task:\n%s\n\n&quot;, bstr);
    }

cleanup:

    if (pScheduler)
        pScheduler-&gt;Release();

    if (pJob)
        pJob-&gt;Release();

    if (pTaskId)
        pTaskId-&gt;Release();

    if (bstr)
        SysFreeString(bstr);
}

// Returns the string associated with the state value.
LPWSTR CJobEventHandler::GetJobStateString(JobState state)
{
    DWORD flag = state;
    DWORD bitPosition = 0;

    for (bitPosition = 0; flag = flag &gt;&gt; 1; bitPosition++)
        ;

    return JobStateStrings[bitPosition];
}


// Returns the string associated with the state value.
LPWSTR CJobEventHandler::GetTaskStateString(TaskState state)
{
    DWORD flag = state;
    DWORD bitPosition = 0;

    for (bitPosition = 0; flag = flag &gt;&gt; 1; bitPosition++)
        ;

    return TaskStateStrings[bitPosition];
}</code></pre></td>
</tr>
</tbody>
</table>



 

 



