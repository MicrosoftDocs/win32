---
Description: 'When you subscribe to command events, you must implement a class that derives from IRemoteCommandEvents.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'acba091b-75cd-4c90-baef-a4039bae3c3f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Implementing the Event Handlers for Command Events in C++
---

# Implementing the Event Handlers for Command Events in C++

When you subscribe to command events, you must implement a class that derives from [**IRemoteCommandEvents**](iremotecommandevents.md). The following C++ example shows a class that implements the [**IRemoteCommandEvents**](iremotecommandevents.md) interface. For an example that shows how to subscribe to the events, see [Executing Commands](executing-commands.md).


```C++
extern HANDLE g_CommandDoneEvent; // Defined in the "Executing Commands" topic's C++ example

// Dispath IDs that identify the methods for the IRemoteCommandEvents interface.
#define DISPID_0NCOMMANDOUTPUT      0x60020000
#define DISPID_ONCOMMANDRAWOUTPUT   0x60020001
#define DISPID_ONCOMMANDTASKSTATE   0x60020002
#define DISPID_ONCOMMANDJOBSTATE    0x60020003


class CCommandEventHandler : public IRemoteCommandEvents
{
    LONG m_lRefCount;
    ITypeInfo* m_pTypeInfo;
    

public:
    // Constructor, Destructor
    CCommandEventHandler()
    {
        m_lRefCount = 1;
        m_pTypeInfo = NULL;
    };

    ~CCommandEventHandler() 
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

    // IRemoteCommandEvents methods
    void __stdcall OnCommandOutput(VARIANT sender, ICommandOutputEventArg* args);
    void __stdcall OnCommandRawOutput(VARIANT sender, ICommandRawOutputEventArg* args);
    void __stdcall OnCommandTaskState(VARIANT sender, ICommandTaskStateEventArg* args);
    void __stdcall OnCommandJobState(VARIANT sender, IJobStateEventArg* args);

private:

    HRESULT LoadTypeInfo(void);
    ISchedulerJob* GetCommandJob(VARIANT sender, long JobId);
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

// IUnknown implementation.

HRESULT CCommandEventHandler::QueryInterface(REFIID riid, LPVOID* ppvObj) 
{
    if (riid == __uuidof(IUnknown) || 
        riid == __uuidof(IDispatch) ||
        riid == __uuidof(IRemoteCommandEvents)) 
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

ULONG CCommandEventHandler::AddRef() 
{
    return InterlockedIncrement(&amp;m_lRefCount);
}

ULONG CCommandEventHandler::Release() 
{
    ULONG  ulCount = InterlockedDecrement(&amp;m_lRefCount);

    if(0 == ulCount) 
    {
        delete this;
    }

    return ulCount;
}

// IDispatch implementation. 

HRESULT __stdcall CCommandEventHandler::GetTypeInfoCount(UINT* pctInfo)
{
    HRESULT hr = S_OK;

    if (pctInfo == NULL) 
        return E_INVALIDARG;

    hr = LoadTypeInfo();

    if (SUCCEEDED(hr))
        *pctInfo = 1;

    return hr;
}

HRESULT __stdcall CCommandEventHandler::GetTypeInfo(UINT itInfo, LCID lcid, ITypeInfo** ppTInfo)
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

HRESULT __stdcall CCommandEventHandler::GetIDsOfNames(REFIID riid, OLECHAR** rgszNames, UINT cNames, LCID lcid, DISPID* rgDispId)
{
    HRESULT hr = S_OK;

    hr = LoadTypeInfo();

    if (FAILED(hr))
        return hr;

    return (m_pTypeInfo-&gt;GetIDsOfNames(rgszNames, cNames, rgDispId));
}

// Invoke the event handler methods directly.
HRESULT __stdcall CCommandEventHandler::Invoke(DISPID dispId, REFIID riid, LCID lcid, WORD wFlags,
    DISPPARAMS* pDispParams, VARIANT* pvarResult, EXCEPINFO* pExcepInfo, UINT* puArgErr)
{
    HRESULT hr = S_OK;
    ICommandOutputEventArg* pOutputArgs = NULL;
    ICommandRawOutputEventArg* pRawOutputArgs = NULL;
    ICommandTaskStateEventArg* pCommandStateArgs = NULL;
    IJobStateEventArg* pJobStateArgs = NULL;
    _variant_t vSender;  
    _variant_t vArgs;


    if (2 != pDispParams-&gt;cArgs) 
        return E_INVALIDARG;

    vSender = pDispParams-&gt;rgvarg[1];  // IScheduler
    vArgs = pDispParams-&gt;rgvarg[0];    // Arguments 

    switch (dispId)
    {
        case DISPID_0NCOMMANDOUTPUT :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_ICommandOutputEventArg, (void**)&amp;pOutputArgs);
            if (SUCCEEDED(hr))
            {
                OnCommandOutput(vSender, pOutputArgs);
                pOutputArgs-&gt;Release();
                pOutputArgs = NULL;
            }
            break;

        case DISPID_ONCOMMANDRAWOUTPUT :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_ICommandRawOutputEventArg, (void**)&amp;pRawOutputArgs);
            if (SUCCEEDED(hr))
            {
                OnCommandRawOutput(vSender, pRawOutputArgs);
                pRawOutputArgs-&gt;Release();
                pRawOutputArgs = NULL;
            }
            break;

        case DISPID_ONCOMMANDTASKSTATE :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_ICommandTaskStateEventArg, (void**)&amp;pCommandStateArgs);
            if (SUCCEEDED(hr))
            {
                OnCommandTaskState(vSender, pCommandStateArgs);
                pCommandStateArgs-&gt;Release();
                pCommandStateArgs = NULL;
            }
            break;

        case DISPID_ONCOMMANDJOBSTATE :
            hr = vArgs.pdispVal-&gt;QueryInterface(IID_IJobStateEventArg, (void**)&amp;pJobStateArgs);
            if (SUCCEEDED(hr))
            {
                OnCommandJobState(vSender, pJobStateArgs);
                pJobStateArgs-&gt;Release();
                pJobStateArgs = NULL;
            }
            break;

        default:
            hr = DISP_E_BADINDEX;  // Bad dispId
    }

    return hr;
}


HRESULT CCommandEventHandler::LoadTypeInfo(void)
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
        hr = pTypeLib-&gt;GetTypeInfoOfGuid(DIID_IRemoteCommandEvents, &amp;m_pTypeInfo);
        pTypeLib-&gt;Release();

        if (FAILED(hr))
            m_pTypeInfo = NULL;
    }

    return hr;
}

// IRemoteCommandEvents implementation.

// The RemoteCommand object will call all event handler methods - there is no way to 
// subscribe to a single event. If you do not want to handle the event, simply return;

void CCommandEventHandler::OnCommandOutput(VARIANT sender, ICommandOutputEventArg* pargs)
{
    HRESULT hr = S_OK;
    BSTR bstrNodeName = NULL;
    BSTR bstrOutput = NULL;


    hr = pargs-&gt;get_NodeName(&amp;bstrNodeName);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }
    
    wprintf(L&quot;\nFormatted line output from %s.\n&quot;, bstrNodeName);

    hr = pargs-&gt;get_Message(&amp;bstrOutput);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    wprintf(L&quot;&lt;%s&gt;\n&quot;, bstrOutput);

cleanup:

    if (bstrNodeName)
        SysFreeString(bstrNodeName);

    if (bstrOutput)
        SysFreeString(bstrOutput);
}

void CCommandEventHandler::OnCommandRawOutput(VARIANT sender, ICommandRawOutputEventArg* pargs)
{
    HRESULT hr = S_OK;
    BSTR bstrNodeName = NULL;
    SAFEARRAY* psaBuffer = NULL;
    PBYTE pData = NULL;
    PBYTE pOutput = NULL;
    long cb = 0;


    hr = pargs-&gt;get_NodeName(&amp;bstrNodeName);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }
    
    wprintf(L&quot;\nRaw output from %s.\n&quot;, bstrNodeName);

    hr = pargs-&gt;get_Output(&amp;psaBuffer);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    if (psaBuffer)
    {
        hr = SafeArrayAccessData(psaBuffer, (void**)&amp;pData);

        cb = psaBuffer-&gt;rgsabound-&gt;cElements * sizeof(byte);

        // The output string is in ASCII, not Unicode.
        pOutput = (PBYTE)malloc(cb + 1);
        if (pOutput)
        {
            memcpy_s(pOutput, cb + 1, pData, cb);
            *(LPSTR)(pOutput+cb) = &#39;\0&#39;;
            wprintf(L&quot;&lt;%S&gt;\n\n&quot;, (LPSTR)pOutput);
            free(pOutput);
            pOutput = NULL;
        }
        else
        {
            // Handle error;
            goto cleanup;
        }
    }

cleanup:

    if (bstrNodeName)
        SysFreeString(bstrNodeName);

    if (pData)
        SafeArrayUnaccessData(psaBuffer);

    if (psaBuffer)
        SafeArrayDestroy(psaBuffer);
}

void CCommandEventHandler::OnCommandTaskState(VARIANT sender, ICommandTaskStateEventArg* pargs)
{
    HRESULT hr = S_OK;
    ITaskStateEventArg* pStateArgs = NULL;
    TaskState State;
    long lExitCode = 0;
    BSTR bstrNodeName = NULL;
    BSTR bstrMessage = NULL;
    VARIANT_BOOL fIsProxyTask = VARIANT_FALSE;


    hr = pargs-&gt;get_IsProxy(&amp;fIsProxyTask);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    // Report state changes for the command, not the proxy task.
    if (VARIANT_FALSE == fIsProxyTask)
    {
        // The state information is contained in the ITaskStateEventArg so you need to query
        // pargs for the interface.
        hr = pargs-&gt;QueryInterface(IID_ITaskStateEventArg, reinterpret_cast&lt;void **&gt; (&amp;pStateArgs));

        hr = pargs-&gt;get_NodeName(&amp;bstrNodeName);
        if (FAILED(hr))
        {
            // Handle error;
            goto cleanup;
        }

        hr = pStateArgs-&gt;get_NewState(&amp;State);
        if (FAILED(hr))
        {
            // Handle error;
            goto cleanup;
        }

        wprintf(L&quot;\nOnCommandTaskState Node: %s State: %s\n&quot;, bstrNodeName, GetTaskStateString(State));

        if (TaskState_Failed == State)
        {
            hr = pargs-&gt;get_ExitCode(&amp;lExitCode);
            if (FAILED(hr))
            {
                // Handle error;
                goto cleanup;
            }

            hr = pargs-&gt;get_ErrorMessage(&amp;bstrMessage);
            if (FAILED(hr))
            {
                // Handle error;
                goto cleanup;
            }

            wprintf(L&quot;Exit code: %ld\nMessage: %s\n&quot;, lExitCode, bstrMessage);
        }
    }

cleanup:

    if (pStateArgs)
        pStateArgs-&gt;Release();

    if (bstrNodeName)
        SysFreeString(bstrNodeName);

    if (bstrMessage)
        SysFreeString(bstrMessage);
}


void CCommandEventHandler::OnCommandJobState(VARIANT sender, IJobStateEventArg* pargs)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    long JobId = 0;
    JobState State;


    hr = pargs-&gt;get_NewState(&amp;State);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

    wprintf(L&quot;\nOnCommandJobState State: %s\n&quot;, GetJobStateString(State));

    // If you need to do something with the job, remove the comments.
    //hr = pargs-&gt;get_JobId(&amp;JobId);
    //if (FAILED(hr))
    //{
    //    // Handle error;
    //    goto cleanup;
    //}

    //pJob = GetCommandJob(sender, JobId);
    //if (NULL == pJob)
    //{
    //    // Handle error;
    //    goto cleanup;
    //}

    // TODO: Do something with the job.

    if (JobState_Finished == State ||
        JobState_Failed == State ||
        JobState_Canceled == State)
    {
        SetEvent(g_CommandDoneEvent);
    }

cleanup:

    if (pJob)
        pJob-&gt;Release();
}


// Called from CCommandEventHandler::OnCommandJobState.
ISchedulerJob* CCommandEventHandler::GetCommandJob(VARIANT sender, long JobId)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    ISchedulerJob* pJob = NULL;


    hr = sender.pdispVal-&gt;QueryInterface(__uuidof(IScheduler), reinterpret_cast&lt;void **&gt; (&amp;pScheduler));

    hr = pScheduler-&gt;OpenJob(JobId, &amp;pJob);
    if (FAILED(hr))
    {
        // Handle error;
        goto cleanup;
    }

cleanup:

    if (pScheduler)
        pScheduler-&gt;Release();

    return pJob;
}



// Returns the string associated with the state value.
LPWSTR CCommandEventHandler::GetJobStateString(JobState state)
{
    DWORD flag = state;
    DWORD bitPosition = 0;

    for (bitPosition = 0; flag = flag &gt;&gt; 1; bitPosition++)
        ;

    return JobStateStrings[bitPosition];
}


// Returns the string associated with the state value.
LPWSTR CCommandEventHandler::GetTaskStateString(TaskState state)
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



 

 



