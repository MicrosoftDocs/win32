---
title: Remote Assistance Sample Code
description: This topic contains sample code that provides IRendezvousSession and DRendezvousSessionEvents implementation. It also shows how to invoke the Component Object Model (COM) objects that implement the IRendezvousApplication interface.
ms.assetid: 4c2e3b87-e434-441a-9bad-8e2838d04113
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remote Assistance Sample Code

This topic contains sample code that provides [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) implementation. It also shows how to invoke the Component Object Model (COM) objects that implement the [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) interface. The sample depends on Active Template Library (ATL) libraries. The sample does not include the transport from one peer to the other. This needs to be implemented by the instant messaging (IM) application.

The following code files and registry information are included in this topic.

-   [RendezvousSessCP.h](#rendezvoussesscph)
-   [RendezvousSessProv.h](#rendezvoussessprovh)
-   [RendezvousSessProv.cpp](#rendezvoussessprovcpp)
-   [RendezvousProv.idl](#rendezvousprovidl)
-   [Registration](#registration)

## RendezvousSessCP.h

The following code shows the implementation of the connection point interface [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/). CRendezvousProv\_Proxy class implements this events interface. The following code should go into the header file for the class that implements the connection point interface and exposes the DRendezvousSession events.


```C++
/*++ 
RendezvousSessCP.h
Abstract:
    Implements the IRendezvousSession, DRendezvousSessionEvents COM interface. 
    This is the header file for the class that implements the connection point
    interface and exposes the DRendezvousSession events. RendezvousApps "Ask for
    Remote Assistance" and "Offer Remote Assistance" can sink the RendezvousSession
    events using IConnectionPoint sink. 
--*/
template <class T, const IID* piid>
class CRendezvousProv_Proxy :
    public IConnectionPointImpl<T, piid, CComDynamicUnkArray>
{

//
// Fire_Event fires events to the COM objects that are subscribed for the events.
//
public:
    VOID Fire_Event(
         IN DISPID dispid, 
         IN DISPPARAMS* pDispParams
         )
    {    
        T* pT = static_cast<T*>(this);
        int nConnectionIndex;
        int nConnections;
        HRESULT hr;
        nConnections = m_vec.GetSize();        
        for (nConnectionIndex = 0;
             nConnectionIndex < nConnections;
             nConnectionIndex++) {
            pT->Lock();
            CComPtr<IUnknown> sp = m_vec.GetAt(nConnectionIndex);
            pT->Unlock();
            IDispatch* pDispatch = reinterpret_cast<IDispatch*>(sp.p);
            if (pDispatch != NULL) {
                hr = pDispatch->Invoke(dispid, 
                                       IID_NULL, 
                                       LOCALE_USER_DEFAULT, 
                                       DISPATCH_METHOD,
                                       pDispParams, NULL, NULL, NULL);
            } // if (pDispatch != NULL)
        } //for
    }

    inline
    VOID Fire_Event(
        IN DISPID dispid, 
        IN VARIANT* pVar=NULL, 
        IN UINT cVarCount=0
        )
    {
        DISPPARAMS DispParams = {pVar, NULL, cVarCount, 0};
        Fire_Event(dispid, &amp;DispParams);
    }  

    inline
    VOID Fire_Event(
        IN DISPID dispid, 
        IN LONG lParam1
        )
    {
        VARIANT var;
        var.vt = VT_I4;
        var.lVal = lParam1;
        
        Fire_Event(dispid, &amp;var, 1);
    }  

    inline
    VOID Fire_Event(
        IN DISPID dispid, 
        IN BSTR lParam1
        )
    {
        VARIANT var;
        var.vt = VT_BSTR;
        var.bstrVal = lParam1;
        
        Fire_Event(dispid, &amp;var, 1);
    }  

    inline
    VOID Fire_Event(
        IN DISPID dispid, 
        IN LONG lParam1,
        IN LONG lParam2
        )
    {
        VARIANT var[2];

        var[0].vt = VT_I4;
        var[0].lVal = lParam2;  

        var[1].vt = VT_I4;
        var[1].lVal = lParam1;
        
        Fire_Event(dispid, var, 2);
    }  

    inline
    VOID Fire_Event(
        IN DISPID dispid, 
        IN LONG lParam1,
        IN BSTR lParam2
        )
    {
        VARIANT var[2];

        var[0].vt = VT_I4;
        var[0].lVal = lParam1;  

        var[1].vt = VT_BSTR;
        var[1].bstrVal = lParam2;
        
        Fire_Event(dispid, var, 2);
    }  

    inline 
    VOID Fire_Event(
        IN DISPID dispid, 
        IN IDispatch* pIDispatch
        )
    {   
        VARIANT var;
        var.vt = VT_DISPATCH;
        var.pdispVal = pIDispatch;
        
        Fire_Event(dispid, &amp;var, 1);
    }

    inline 
    VOID Fire_Event(
        IN DISPID dispid, 
        IN IDispatch* pIDispatch,
        IN LONG       lParam
        )
    {   
        VARIANT var[2];

        var[0].vt = VT_I4;
        var[0].lVal = lParam;

        var[1].vt = VT_DISPATCH;
        var[1].pdispVal = pIDispatch;
        
        Fire_Event(dispid, var, 2);
    }

    inline 
    VOID Fire_Event(
        IN DISPID     dispid, 
        IN IUnknown*  pIUnk,
        IN long       lVal, 
        IN BSTR       bstr
        )
    {   
        VARIANT var[3];
        
        var[2].vt      = VT_UNKNOWN;
        var[2].punkVal = pIUnk;

        var[1].vt = VT_I4;
        var[1].lVal = lVal;
        
        var[0].vt      = VT_BSTR;
        var[0].bstrVal = bstr;
        
        Fire_Event(dispid, var, 3);
    }

    inline 
    VOID Fire_Event(
        IN DISPID     dispid, 
        IN IUnknown*  pIUnk,
        IN long       lVal1,
        IN long       lVal2
        )
    {   
        VARIANT var[3];
        
        var[2].vt      = VT_UNKNOWN;
        var[2].punkVal = pIUnk;

        var[1].vt = VT_I4;
        var[1].lVal = lVal1;
        
        var[0].vt = VT_I4;
        var[0].lVal = lVal2;
        
        Fire_Event(dispid, var, 3);
    }

    inline 
    VOID Fire_Event(
        IN DISPID     dispid,
        IN long       lVal1,
        IN long       lVal2,
        IN long       lVal3,
        IN long       lVal4
        )
    {   
        VARIANT var[4];

        var[3].vt   = VT_I4;
        var[3].lVal = lVal1;
        
        var[2].vt   = VT_I4;
        var[2].lVal = lVal2;

        var[1].vt   = VT_I4;
        var[1].lVal = lVal3;
        
        var[0].vt   = VT_I4;
        var[0].lVal = lVal4;
        
        Fire_Event(dispid, var, TSARRAYSIZE(var));
    }

    
};
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```



## RendezvousSessProv.h

The following code should go into the header file of the object implementing the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) interface. CRendezvousProv is the class that implements **IRendezvousSession** interface.


```
/*++ 

Module Name:

    RendezvousSessProv.h

Abstract:
    This is the header file for the class that implements IRendezvousSession.
    
--*/

#pragma once

//
// The header to fire events through IConnectionPoint sinks. 
// 
#include "RendezvousSessCP.h"

//
// For DIID_DRendezvousSessionEvents
//
#include "RendezvousSession_i.c"
/////////////////////////////////////////////////////////////////////////////
// CRendezvousSessProv

class CRendezvousSessProv : 
    public CComObjectRootEx<CComMultiThreadModel>,
    public CComCoClass<CRendezvousSessProv, &amp;__uuidof(RendezvousSim)>,
    public IConnectionPointContainerImpl<CRendezvousSessProv>,
    public CRendezvousProv_Proxy<CRendezvousSessProv, &amp;DIID_DRendezvousSessionEvents>,
    public IRendezvousSim,
    public IRendezvousSession
{

public:
    CRendezvousSessProv() :
        m_bInviter(FALSE),
        m_bInvitee(FALSE)
        {}
        
    ~CRendezvousSessProv()
    {
  
    }

//
// Required for OBJECT_ENTRY_AUTO
//
DECLARE_REGISTRY_RESOURCEID(IDR_RENDEZVOUSPROV) 
DECLARE_PROTECT_FINAL_CONSTRUCT()
BEGIN_COM_MAP(CRendezvousSessProv)
    COM_INTERFACE_ENTRY(IRendezvousSim)
    COM_INTERFACE_ENTRY(IRendezvousSession)
    COM_INTERFACE_ENTRY(IConnectionPointContainer)
END_COM_MAP()

BEGIN_CONNECTION_POINT_MAP(CRendezvousSessProv)
    CONNECTION_POINT_ENTRY(DIID_DRendezvousSessionEvents)
END_CONNECTION_POINT_MAP()

//
// IRendezvousSession 
//
public:

    virtual HRESULT 
    FinalConstruct();

    virtual HRESULT 
    FinalRelease();


    //
    // CoCreates the RendezvousApp based on the bstrRendezvousGuid.
    // Sets up the Peer/Buddy as server or client depending on the BOOL 
    // bServer.
    //
    STDMETHOD(Init)(__in BSTR bstrRendezvousGuid, __in BOOL bServer, __in BOOL bRequest);

  //
    // Returns the current state. It is one of the values defined in 
    // RENDEZVOUS_SESSION_STATE - look up RendezvousSession.h
    // for the possible states.
    //
    STDMETHOD(get_State)(__out RENDEZVOUS_SESSION_STATE *pState);

    //
    // Returns the name of the remote peer/buddy as a BSTR.
    //
    STDMETHOD(get_RemoteUser)(__out BSTR *pbstr);

    //
    // Returns the flags associated with the session used to tell if 
    // the Peer/Buddy is the inviter / invitee, etc. One or more bits
    // in RENDEZVOUS_SESSION_FLAGS as defined in RendezvousSession.h
    // can be set.
    //
    STDMETHOD(get_Flags)(__out LONG *plFlags);

    //
    // Sends bstrData to the Remote Peer/Buddy. The actual transport is based 
    // on sockets.
    //
    STDMETHOD(SendContextData)(__in BSTR bstrData);

    //
    // The RendezvousApp calls the Terminate method and the rendezvous
    // session provider can then release the reference to the RendezvousApp.
    //
    STDMETHOD(Terminate)(__in HRESULT hr, __in BSTR bstrAppData);

//
// members
//
protected:

    RENDEZVOUS_SESSION_STATE    m_SessionState;
    CComBSTR                    m_bstrRemoteUser;
    CComBSTR                    m_bstrExpertMacName;
    LONG                        m_Flags;
    BOOL                        m_bInviter;
    BOOL                        m_bInvitee;
    SOCKET                      m_Socket;

};

OBJECT_ENTRY_AUTO(__uuidof(RendezvousSim), CRendezvousSessProv)

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```



## RendezvousSessProv.cpp

This file contains the code for the class that provides the implementation for [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) and [**DRendezvousSessionEvents**](/previous-versions/windows/desktop/api/RendezvousSession/) public interfaces. Given a specific RendezvousComponent COM GUID it cocreates and launches the COM object. The actual transport of the data between the two [**IRendezvousApplication**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvousapplication) based peers needs to be implemented by the IM provider. The IM provider should also provide a way to launch the RendezvousApplications from within IM UI.


```
/*++ 
Module Name:
RendezvousSessProv.cpp
Abstract:
 This is the .cpp file contains the code for the class that provides the implementation for IRendezvousSession and DRendezvousSessionEvents public interfaces. Given a specific RendezvousComponent COM GUID it CoCreates and launches the COM object. The actual transport of the data between the two IRendezvousApplication based peers needs to be implemented by the IM provider. The IM provider should also provide a way to launch the RendezvousApplications from within IM UI.
--*/
#include "stdafx.h"

//
// CoCreates the RendezvousApp based on the bstrRendezvousGuid.
//
HRESULT CRendezvousSessProv::Init(BSTR bstrRendezvousGuid, BOOL bNovice, BOOL bRequest)
{
    HRESULT                         hr = S_OK;
    GUID                            guid;
    CComPtr<IRendezvousApplication> spRendezvousApp;

   if (bstrRendezvousGuid == NULL || *bstrRendezvousGuid == '\0') {
        hr = E_INVALIDARG;
        goto done;
    }

    hr = CLSIDFromString(bstrRendezvousGuid, &amp;guid);
    if(FAILED(hr)) {
        goto done;
    }

    hr = spRendezvousApp.CoCreateInstance(guid);
    if(FAILED(hr)) {
        goto done;
    }

   if(bNovice) {
        if(bRequest) {
                //
             //  Request, Novice Mode  = Inviter 
                //
                m_bInviter = TRUE;
                m_bInvitee = FALSE;
         } else {
            //
            //  Offer, Novice Mode  = Invitee
            //
            m_bInvitee = TRUE;
            m_bInviter = FALSE;
        }
    } else {
        if(bRequest) {
            //
            //  Request, Expert Mode  = Invitee
            //
            m_bInvitee = TRUE;
            m_bInviter = FALSE;
            
        } else {
            //
            //  Offer, Expert Mode  = Inviter
            //
            m_bInviter = TRUE;
            m_bInvitee = FALSE;
        }
    }

    //
    // Initialize the Session State
    //
    m_SessionState = RSS_CONNECTED;

    //
    //  Call the RendezvousApp's SetRendezvousSession to pass the control to the 
    //  RendezvousApp
    //
    hr = spRendezvousApp->SetRendezvousSession(static_cast<IRendezvousSession*>(this));
    

    }

done:
    return hr;
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Events are fired using the following format
Fire_Event(DISPID_EVENT_ON_CONTEXT_DATA, pbstrPacket);


HRESULT CRendezvousSessProv::FinalConstruct()
{     
    HRESULT hr;
    
    hr = S_OK;
    
    return hr;
}

HRESULT CRendezvousSessProv::FinalRelease()
{
   
    return S_OK;
}

//
// Returns the current state. It is one of the values defined in 
// RENDEZVOUS_SESSION_STATE - look up RendezvousSession.h
// for the possible states.
//

HRESULT CRendezvousSessProv::get_State( __out RENDEZVOUS_SESSION_STATE *pState) 
{ 
    HRESULT hr = S_OK;

    if(!pState) {
        hr = E_POINTER;
    } else {
        *pState = m_SessionState;
    }
    return hr;
}


//
// Returns the flags associated with the session used to tell if 
// the Peer/Buddy is the inviter / invitee, etc. One or more bits
// in RENDEZVOUS_SESSION_FLAGS as defined in RendezvousSession.h
// can be set.
//
HRESULT CRendezvousSessProv::get_Flags( __out LONG *plFlags)
{
    
    HRESULT hr = S_OK;

    if (!plFlags){
        hr = E_POINTER;
    } else {
        
        *plFlags = 0;
        if(m_bInviter == TRUE) {
            *plFlags = RSF_INVITER;
        } else if (m_bInvitee == TRUE) {
            *plFlags = RSF_INVITEE;
        }
    }

    return hr;
}

//
// Returns the name of the remote peer/buddy as a BSTR.
//
HRESULT CRendezvousSessProv::get_RemoteUser( __out BSTR *pbstrUser)
{
    HRESULT hr = S_OK;
    
    if (pbstrUser == NULL){

        hr = E_POINTER;

    } else {

        *pbstrUser = m_bstrRemoteUser.Copy();
    }

    return hr;
}

///
///
/// Implementation of IRendezvousSession::SendContextData
///
HRESULT CRendezvousSessProv::SendContextData( 
    /* [in] */ BSTR bstrData)
{
    HRESULT         hr = S_OK;
    char*           Buffer;
    unsigned int    uiSize = 0;
    unsigned int    cbPacketLen;
    int             DataSize = 0;
    BSTR            pbstrLengthPrefixedData;
    DWORD           dwSize;
        
    Buffer = Allocate(MAX_XFER_SIZE);
    uiSize = ::SysStringByteLen(bstrData);

    cbPacketLen = uiSize+sizeof(DataSize);
    dwSize = uiSize;

    //
    // Allocate the BSTR
    //
    pbstrLengthPrefixedData  = ::SysAllocStringByteLen(NULL, cbPacketLen);
    if(pbstrLengthPrefixedData){
        memset(pbstrLengthPrefixedData, 0, cbPacketLen);
    } else {
        hr = E_OUTOFMEMORY;
    }

    //
    // Copy the Size of the Data
    //
    *(PDWORD)(pbstrLengthPrefixedData) = dwSize;

    //
    // Copy the actual data BSTR
    //
    memcpy((PBYTE)(pbstrLengthPrefixedData) + sizeof(DWORD), 
                bstrData, 
                ::SysStringByteLen(bstrData));

     
    //
    // Get the Buffer ready
    //
    memcpy((PBYTE)(Buffer) , 
                pbstrLengthPrefixedData, 
                cbPacketLen);

//

 //
//   The IM provider should use its own transport to send data across to the remote IM Buddy. 
//
 SendData(Buffer, cbPacketLen);

    return hr;
}

///
///
/// Implementation of IRendezvousSession::Terminate
///
HRESULT CRendezvousSessProv::Terminate(HRESULT hrSend, BSTR bstrAppData)
{
    HRESULT hr = S_OK;
    
    hrSend = hr;
   Fire_Event(DISPID_EVENT_ON_TERMINATION, (long)hrSend, bstrAppData);
   return S_OK;
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```



## RendezvousProv.idl

This is the Interface Definition Language (IDL) source for RendezvousSim that implements the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) provider to integrate Request RA and Offer RA Rendezvous applications.


```
RendezvousProv.idl
// The following is the code from the IDL file. 
// RendezvousProv.idl : IDL source for RendezvousSim
// Implements the IRendezvousSession provider to integrate
// Request RA and Offer RA Rendezvous applications.
//
// This file will be processed by the MIDL tool to
// produce the type library (RendezvousSim.tlb) and marshalling code.

import "oaidl.idl";
import "ocidl.idl";

import "RendezvousSession.idl";

[
    object,
    uuid(7182BE78-C74D-4088-AD4A-10F04464FAD6),
    oleautomation,
    nonextensible,
    helpstring("IRendezvousSim Interface"),
    pointer_default(unique)
]
interface IRendezvousSim : IUnknown {

    [
    ]
    HRESULT 
    Init(
        [in] BSTR bstrRendezvousGuid,
        [in] BOOL bNovice,
        [in] BOOL bRequest
    );

//
// Any additional methods, properties required by the IM provider COM object go here
//

};
[
    uuid(89359B7A-D1D6-477a-82C5-C85672DE3213),
    version(1.0),
    helpstring("RendezvousSim 1.0 Type Library")
]
library RendezvousSim
{
    importlib("stdole2.tlb");
    [
        uuid(6D109173-6F3D-4418-B3FE-52FA0BA96AF7),
        helpstring("RendezvousSim Class")
    ]
    coclass RendezvousSim
    {
        interface IRendezvousSim;
        [default] interface IRendezvousSession;
        [default, source] dispinterface DRendezvousSessionEvents;
    };
};
```



## Registration

The following is the COM object registration of the [**IRendezvousSession**](/previous-versions/windows/desktop/api/RendezvousSession/nn-rendezvoussession-irendezvoussession) based object.


```
//
// Registry information to be added to the windows registry
//

Windows Registry Editor Version 5.00

;;;; CLSID
    
[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}]
@="RendezvousSim class" 

[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}\LocalServer32]
@="c:\\windows\\system32\\RendezvousSim.exe"

[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}\ProgID]
@="RendezvousSim.RendezvousProv.1"

[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}\TypeLib]
@="{89359B7A-D1D6-477a-82C5-C85672DE3213}"

[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}\VersionIndependentProgID]
@="RendezvousSim.RendezvousProv"

[HKEY_CLASSES_ROOT\CLSID\{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}\Version]
@="1.0"


;;;; Interface           
    
[HKEY_CLASSES_ROOT\Interface\{7182BE78-C74D-4088-AD4A-10F04464FAD6}]
@="IRendezvousSim"

[HKEY_CLASSES_ROOT\Interface\{7182BE78-C74D-4088-AD4A-10F04464FAD6}\ProxyStubClsid32]
@="{00020424-0000-0000-C000-000000000046}"

[HKEY_CLASSES_ROOT\Interface\{7182BE78-C74D-4088-AD4A-10F04464FAD6}\TypeLib]
@="{89359B7A-D1D6-477a-82C5-C85672DE3213}"
"Version"="1.0"

;;;; ProgId
    
[HKEY_CLASSES_ROOT\RendezvousSim.RendezvousProv]
@="RendezvousSim"

[HKEY_CLASSES_ROOT\RendezvousSim.RendezvousProv\CLSID]
@="{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}"

[HKEY_CLASSES_ROOT\RendezvousSim.RendezvousProv\CurVer]
@="RendezvousSim.RendezvousProv.1"

[HKEY_CLASSES_ROOT\RendezvousSim.RendezvousProv.1]
@="RendezvousSim class"

[HKEY_CLASSES_ROOT\RendezvousSim.RendezvousProv.1\CLSID]
@="{6D109173-6F3D-4418-B3FE-52FA0BA96AF7}"
    

;;;; TypeLib
                        
[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}]
@=""

[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}\1.0]
@="RendezvousSim 1.0 Type Library"

[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}\1.0\9]

[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}\1.0\9\win32]
@="c:\\windows\\system32\\RendezvousSim.exe"

[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}\1.0\FLAGS]
@="0"

[HKEY_CLASSES_ROOT\TypeLib\{89359B7A-D1D6-477a-82C5-C85672DE3213}\1.0\HELPDIR]
@=""
```



 

 




