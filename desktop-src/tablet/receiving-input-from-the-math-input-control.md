---
description: This section explains how to retrieve the MathML markup from the math input control using the Active Template Library (ATL) and the Component Object Model (COM).
ms.assetid: 352d2a0c-8275-4fe4-b523-4c74126ffadf
title: Receiving Input from the Math Input Control
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Input from the Math Input Control

This section explains how to retrieve the MathML markup from the math input control using the Active Template Library (ATL) and the Component Object Model (COM).

To retrieve the recognized math equation from the math input control, you can override the behavior that happens when the insert button is pressed. To do this, you will need to set up an event handler that implements the various events that are supported by the [**\_IMathInputControlEvents**](/windows/win32/api/micaut/nn-micaut-_imathinputcontrolevents) interface. Setting up the events handler involves the performing the following steps for the events you want to support (insert in this case).

-   [Create a template class that contains event sinks](#create-a-template-class-that-contains-event-sinks)
-   [Set up the event handlers](#set-up-the-event-handlers)
-   [Inherit the event handler class in your main class](#inherit-the-event-handler-class-in-your-main-class)
-   [Initialize your class to inherit the event sink(s)](#initialize-your-class-to-inherit-the-event-sinks)

## Create a template class that contains event sinks

When you are implementing an event sink that uses the math input control, you must first specify a sink id. You must then create a template class that inherits from the event, event control handler, and math input control event interfaces. The following code shows how to set a sink id and create such a template class, CMathInputControlEventHandler, that inherits from the requisite interfaces. This template class also is set up to have a private unknown interface pointer that will be used to pass the math input control to it on initialization and the m\_ulAdviseCount member to count the number of calls to advise / unadvise.


```
  
#pragma once
static const int MATHINPUTCONTROL_SINK_ID = 1 ;

template <class T>
class ATL_NO_VTABLE CMathInputControlEventHandler :
    public IDispEventSimpleImpl<MATHINPUTCONTROL_SINK_ID, CMathInputControlEventHandler<T>, &__uuidof(_IMathInputControlEvents)>
{
private:
    IUnknown    *m_pUnknown;
    ULONG m_ulAdviseCount;
    CDialog *m_pMain;

```



> [!Note]  
> The member **m\_pMain** should be different in your implementation if you are not using a dialog.

 

Now that you have the basic template class, you must give a forward declaration for the event handlers that you will be overriding and must then set up a sink map for the events you will be handling. The following code shows how to set up event handlers for the [**Insert**](/previous-versions/windows/desktop/legacy/dd317352(v=vs.85)) method, called when a user clicks the insert button on the math input control, and the [**Close**](/previous-versions/windows/desktop/legacy/dd317351(v=vs.85)) method, called when a user clicks the cancel button on the math input control.


```
  
public:
    static const _ATL_FUNC_INFO OnMICInsertInfo; // = {CC_STDCALL, VT_I4, 1, {VT_BSTR}};
    static const _ATL_FUNC_INFO OnMICCloseInfo;  // = {CC_STDCALL, VT_I4, 0, {VT_EMPTY}};

    BEGIN_SINK_MAP(CMathInputControlEventHandler)
        SINK_ENTRY_INFO(MATHINPUTCONTROL_SINK_ID, __uuidof(_IMathInputControlEvents), DISPID_MICInsert, OnMICInsert, const_cast<_ATL_FUNC_INFO*>(&OnMICInsertInfo))
        SINK_ENTRY_INFO(MATHINPUTCONTROL_SINK_ID, __uuidof(_IMathInputControlEvents), DISPID_MICClose, OnMICClose, const_cast<_ATL_FUNC_INFO*>(&OnMICCloseInfo))  
    END_SINK_MAP()
```



Since you will be working with the math input control, it will be useful to set an internal reference to the relevant interface. The following utility function is created in the example class to set this reference.


```
    
  HRESULT Initialize(IUnknown *pUnknown, CDialog *pMain)
  {
    m_pMain  = pMain;
    m_pUnknown = pUnknown;
    m_ulAdviseCount = 0;
    return S_OK;
  }
  
```



## Set up the event handlers

Once you have set up the event sinks, you will need to create your implementations of the event sinks. In both of the methods in the following code example, the event sinks retrieve a handle to the math input control interface. In the [**Insert**](/previous-versions/windows/desktop/legacy/dd317352(v=vs.85)) function, the recognition result is displayed as MathML and the control is hidden. In the [**Close**](/previous-versions/windows/desktop/legacy/dd317351(v=vs.85)) function, the math input control is hidden.


```
  
    // Methods
    HRESULT __stdcall OnMICInsert( BSTR bstrRecoResult)
    {
        CComQIPtr<IMathInputControl> spMIC(m_pUnknown);
        HRESULT hr=S_OK;
        if (spMIC)
        {           
            MessageBox(NULL,bstrRecoResult,L"Recognition Result",MB_OK);
            hr = spMIC->Hide();
            return hr;  
        }
        return E_FAIL;          
    }

    HRESULT __stdcall OnMICClose()
    {
        CComPtr<IMathInputControl> spMIC;
        HRESULT hr = m_pUnknown->QueryInterface<IMathInputControl>(&spMIC);
        if (SUCCEEDED(hr))
        {           
            hr = spMIC->Hide();
            return hr;  
        }
        return hr;                  
    }
};  
```



## Inherit the event handler class in your main class

After you have your template class implemented, you will need to inherit it into the class that you will be setting up your math input control in. For the purposes of this guide, this class is a dialog, CMIC\_TEST\_EVENTSDlg. In the dialog header, the requisite headers must be included and the template class you created must be inherited. The class you're inheriting within and the event handlers must have forward declarations so that the template can be implemented. The following code example shows how this is done.


```
#pragma once
#include <atlbase.h>
#include <atlwin.h>

// include for MIC
#include "micaut.h"

// include for event sinks
#include <iacom.h>
#include "mathinputcontroleventhandler.h"

class CMIC_TEST_EVENTSDlg;

const _ATL_FUNC_INFO CMathInputControlEventHandler<CMIC_TEST_EVENTSDlg>::OnMICInsertInfo = {CC_STDCALL, VT_I4, 1, {VT_BSTR}};
const _ATL_FUNC_INFO CMathInputControlEventHandler<CMIC_TEST_EVENTSDlg>::OnMICCloseInfo = {CC_STDCALL, VT_I4, 0, {VT_EMPTY}};

// CMIC_TEST_EVENTSDlg dialog
class CMIC_TEST_EVENTSDlg : public CDialog,
    public CMathInputControlEventHandler<CMIC_TEST_EVENTSDlg>
{
  public:
  CComPtr<IMathInputControl> m_spMIC; // Math Input Control

  
```



> [!Note]  
> The template type, **CMIC\_TEST\_EventsDlg**, will be different unless you have named your class the same as the example.

 

## Initialize your class to inherit the event sink(s)

Once you have set up your class to inherit from the template class, you are ready to set it up to handle events. This will consist of initializing the class to have a handle to the math input control and the calling class. Additionally, the math input control to handle events from must be sent to the DispEventAdvise method that the CMathInputControlEventHandler example class inherits. The following code is called from the OnInitDialog method in the example class to perform these actions.


```
// includes for implementation
#include "micaut_i.c"

// include for event handler
#include "mathinputcontroleventhandler.h"

...

OnInitDialog{
  ...

  // TODO: Add extra initialization here
  CoInitialize(NULL);
  HRESULT hr = g_spMIC.CoCreateInstance(CLSID_MathInputControl);
  if (SUCCEEDED(hr)){
    hr = CMathInputControlEventHandler<CMIC_TEST_EVENTSDlg>::Initialize(m_spMIC, this);
      if (SUCCEEDED(hr)){
        hr = CMathInputControlEventHandler<CMIC_TEST_EVENTSDlg>::DispEventAdvise(m_spMIC);            
        if (SUCCEEDED(hr)){
          hr = m_spMIC->Show();  
        }
      }
    }
  }  
}
  
```



> [!Note]  
> The template type, CMIC\_TEST\_EventsDlg in this example, will be different unless you have named your class the same as the example.

 

 

 
