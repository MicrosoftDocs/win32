---
title: Example SHV
description: The following example sets up a system health validator (SHV) on a NAP health policy server.
ms.assetid: 2264c1d7-b1fb-4937-bf24-d6fa05bdc6fe
ms.topic: article
ms.date: 05/31/2018
---

# Example SHV

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The following example sets up a system health validator (SHV) on a NAP health policy server.

> [!Note]  
> The NAP SDK also contains a full set of sample code that can be found in the ...\\Samples\\NetDS\\NAP... directory of your SDK installation. This sample set includes and system health agent (SHA), SHV, and enforcement client (EC). It has full working NAP scenarios setting up communication between SHA-SHV and SHA-EC.

 


```C++
#include <windows.h>
#include "stdafx.h"
#include "NapUtil.h"
#include "NapTypes.h"
#include "NapProtocol.h"
#include "NapMicrosoftVendorIds.h"
#include "NapSystemHealthValidator.h"
#include "NapError.h"

STDMETHODIMP CSampleShv::Validate(
    /*[in]*/ INapSystemHealthValidationRequest* pShvRequest,
    /*[in]*/ UINT32 hintTimeOutInMsec,
    /*[in]*/ INapServerCallback* pCallback)

{
    HRESULT hr = S_OK;

    //
    // SDK Note:
    //
    // If a SoH validation code determines that it needs to contact an external 
    // server to assist with validation, it must start a separate helper thread
    // to contact the server, and return E_PENDING in this thread. When that 
    // occurs, this thread must exit to the SHV Host, returning the E_PENDING 
    // result; the helper thread should independently determine the final 
    // validation result, generate the response SoH, and call the SHV Host's 
    // Callback interface.
    //
    // This SHV handles the Validate() call asynchronously. Validate() method 
    // return with hr = E_PENDING and does the processing of SoH request and 
    // generating SoHResponse in a separate thread.

    //
    // SDK Note:
    //
    // If a SHV does not require processing in a separate thread but can return 
    // the response immediately, it should call the function QShvRespondSHVHost() 
    // below.

    // Store the callback and request pointers.
    m_pShvRequest = pShvRequest;
    m_callback = pCallback;

    //
    // SDK Note:
    //
    // Creating a separate helper thread is done whenever a SHV must contact 
    // the external server. Therefore, the following code that creates a thread 
    // should be executed whenever the need arises.
    //
    // Here we assume the SHV will always contact an external server. Therefore,
    // create the thread at the very start and do all the processing in the helper
    // thread.
    
    // Create Thread to process the SoHRequest and reply with SoHResponse.
    hr = QShvCreateThread();

    // AddRef the request and callback pointers.
    pShvRequest->AddRef();
    pCallback->AddRef();

    return hr;
}

// Creates a thread for asynchronous handling of the Validate() call.
HRESULT CSampleShv::QShvCreateThread()
{
    HRESULT hr = S_OK;
    threadHandle = NULL;
    DWORD threadId = 0;

    // Windows API to create a thread.
    threadHandle = (HANDLE) CreateThread( NULL, 0, AsyncThreadHandler, (LPVOID) this, 
                                          0, &threadId );
    //
    // SDK Note:
    //
    // Here we assume the thread was created successfully and respond with status =       
    // E_PENDING to the SHV Host. 
    hr = E_PENDING;
    return hr;
}

// This is the thread handler. The input parameter is the pointer to this object.
DWORD CSampleShv::AsyncThreadHandler(LPVOID lpParameter)
{
    DWORD errCode = ERROR_SUCCESS;
    errCode = reinterpret_cast<CSampleShv *>(lpParameter)->AsyncThreadHandlerMain(); 
    return errCode;
}

// The thread handler calls this method that has access to member variables.
DWORD __stdcall CSampleShv::AsyncThreadHandlerMain()
{
    DWORD errCode = ERROR_SUCCESS;
    HRESULT hr = S_OK;
    hr = QShvRespondSHVHost();
    CloseHandle(threadHandle);
    errCode = HRESULT_CODE(hr);
    return errCode;        
}

// Handles processing of incoming SoH Request and generating SoH Response.
HRESULT CSampleShv::QShvRespondSHVHost()
{
    HRESULT hr = S_OK;
    hr = HandleRequestSoH(m_pShvRequest);
    if (FAILED(hr))
    {
        //
        // SDK Note:
        //
        // If errors occur here, do not terminate this method -- the SHV should
        // still generate an SoH response.
    }
    hr = HandleResponseSoH(hr, m_pShvRequest);

    // SoH Response is now set. Calling OnComplete() notifies setting of SoHResponse.
    hr = m_callback->OnComplete(m_pShvRequest, hr);

    // Release the request and callback pointers.
    m_pShvRequest->Release();
    m_callback->Release();

    return hr;    
}

// Perform all handling of inbound SoH requests from clients.
HRESULT CSampleShv::HandleRequestSoH(INapSystemHealthValidationRequest* pShvRequest) throw()
{
    HRESULT hr = S_OK;
    SoH *pSohRequest = NULL;
    INapSoHProcessor *pSohProcessor = NULL;
    SystemHealthEntityId systemHealthId = 0;
    BOOL napAgentGenerated = FALSE;

    // Obtain the client's SoH data from the SHV Host.
    hr = pShvRequest->GetSoHRequest(&pSohRequest, &napAgentGenerated);
     
    // Wrap it inside an INapSoHProcessor object.
    hr = CreateInputSoHProcessor(pSohProcessor, systemHealthId, SOH_REQUEST, pSohRequest);

    // Verify whether the client's SoH request data is considered "healthy".
    hr = CheckRequestSoHHealth(systemHealthId, pSohProcessor);

    // Release the SoH handler object.
    ReleaseObject(pSohProcessor);

    // Free the temporary SoH struct.
    FreeSoH(pSohRequest);

    return hr;
}


// Verify whether the client's SoH data is considered healthy.
HRESULT CSampleShv::CheckRequestSoHHealth( SystemHealthEntityId systemHealthId, 
                                           INapSoHProcessor *pSohRequest) throw()
{
    HRESULT hr = S_OK;

    //
    // SDK Note:
    //
    // Each vendor should update this method & its helper functions, based upon their 
    // own business logic.

    // Sanity check -- if no SoH data was passed in, leave client data unset.
    if (! pSohRequest)
    {
        //
        // SDK Note:
        //
        //  - If this SHV is acting as an intrusion detection system, it
        //    should use its specific business logic to determine whether
        //    the client is trusted or malicious, and should create an
        //    SoH Response containing the appropriate error code to
        //    convey the result to the SHV Host.
        //  - All other SHVs should return NAP_E_MISSING_SOH.

        hr = NAP_E_MISSING_SOH;
        goto Cleanup;
    }

    //
    // SDK Note:
    //
    // Check for the existence and values for each attribute that are expected 
    // from the client and determine if the client is healthy or needs to be 
    // quarantined.

    Cleanup:
        return hr;
}

// Perform all handling of outbound SoH responses sent back to clients.
HRESULT CSampleShv::HandleResponseSoH(HRESULT validationResult, 
                                      INapSystemHealthValidationRequest* pShvRequest) throw()
{
    HRESULT hr = S_OK;
    INapSoHConstructor *pSohConstructor = NULL;
    SoH *pSohResponse = NULL;

    // Create an empty SoH response.
    hr = CreateOutputSoHConstructor(pSohConstructor, QuarSampleSystemHealthId, SOH_RESPONSE);

    // Populate the SoH response based on the client's health state.
    hr = FillResponseSoH(validationResult, pSohConstructor);

    // Get portable SoH interface.
    hr = pSohConstructor->GetSoH(&pSohResponse);
    if (! pSohResponse){
        hr = E_POINTER; 
    }

    // Pass the SoH response along to the SHV Host where it is saved.
    hr = pShvRequest->SetSoHResponse(pSohResponse);

    // Release the SoH handler object.
    ReleaseObject(pSohConstructor);

    // Free the temporary SoH struct.
    FreeSoH(pSohResponse);

    return hr;
}

// Fill the specified response SoH object, given the current client's health state.
HRESULT CSampleShv::FillResponseSoH(HRESULT validationResult, 
                                    INapSoHConstructor* &pSohResponse) throw()
{
    HRESULT hr = S_OK;
    SoHAttributeValue value = {0};

    //
    // SDK Note:
    //
    // Append the manditory attribute: Compliance Result Codes. If SHV was not able to 
    // contact the external server (due to network failure, the is server down, etc...),
    // then the SHV should return the failure category attribute instead of the 
    // compliance result with FailureCategory = failureCategoryServerCommunication. 
    // Here we assume there is no such failure.

    value.codesVal.count = 1;
    value.codesVal.results = &validationResult;
    hr = pSohResponse->AppendAttribute(sohAttributeTypeComplianceResultCodes, &value);
    ZeroMemory(&value, sizeof(value));

    //
    // Append any optional attributes.
    //

    return hr;
}
```



 

 




