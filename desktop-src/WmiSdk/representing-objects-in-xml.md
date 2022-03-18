---
description: Generates XML representations of objects.
ms.assetid: 06d2b532-7ab2-489d-9021-27b5187c8f2b
ms.tgt_platform: multiple
title: Representing Objects in XML
ms.topic: article
ms.date: 05/31/2018
---

# Representing Objects in XML

The XML encoder component in WMI generates XML representations of objects.

In C++, you can start the XML encoder with a call to the [**IWbemObjectTextSrc.GetText**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjecttextsrc-gettext) method, specifying the object to be represented in XML and the text format to use in the representation. For more information and a code example, see To encode an object in XML using C/C++.

In VBScript or Visual Basic, to encode data for an XML instance, call [**SWbemObjectEx.GetText**](swbemobjectex-gettext-.md). For more information and a code example, see To encode an object in XML using VBScript.

The following sections are discussed in this topic:

-   [Encode an Object Using C or C++](#encode-an-object-using-c-or-c)
-   [Encode an Object Using VBScript](#encode-an-object-using-vbscript)
-   [Related topics](#related-topics)

## Encode an Object Using C or C++

<span id="to_encode_an_object_in_xml_using_c_c_"></span><span id="TO_ENCODE_AN_OBJECT_IN_XML_USING_C_C_"></span>

The following procedure describes how to encode an object in XML using C or C++.

**To encode an object in XML using C or C++**

1.  Set up your program to access WMI data.

    Because WMI is based on COM technology, you must perform the requisite calls to the [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) functions to access WMI. For more information, see [Initializing COM for a WMI Application](initializing-com-for-a-wmi-application.md).

2.  Optionally, create an [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object and initialize it.

    You do not need to create the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object unless you need to change the default operation. The context object is used by the XML encoder to control the amount of information included in the object's XML representation.

    The following table lists the optional values that can be specified for the context object.

    

    <table>
    <thead>
    <tr class="header">
    <th>Value/type</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>&quot;LocalOnly&quot; <strong>VT_BOOL</strong></td>
    <td>When <strong>TRUE</strong>, only properties and methods defined locally in the class are present in the resulting XML. The default value is <strong>FALSE</strong>.</td>
    </tr>
    <tr class="even">
    <td>&quot;IncludeQualifiers&quot; <strong>VT_BOOL</strong></td>
    <td>When <strong>TRUE</strong>, class, instance, properties, and method qualifiers are included in the resulting XML. The default value is <strong>FALSE</strong>.</td>
    </tr>
    <tr class="odd">
    <td>&quot;ExcludeSystemProperties&quot; <strong>VT_BOOL</strong></td>
    <td>When <strong>TRUE</strong>, WMI system properties are filtered out of the output. The default value is <strong>FALSE</strong>.</td>
    </tr>
    <tr class="even">
    <td>&quot;PathLevel&quot; <strong>VT_I4</strong></td>
    <td><dl> 0 = A &lt;CLASS&gt; or \<INSTANCE> element is generated.<br />
    1 = A <VALUE.NAMEDOBJECT> element is generated.<br />
    2 = A <VALUE.OBJECTWITHLOCALPATH> element is generated.<br />
    3 = A <VALUE.OBJECTWITHPATH> is generated.<br />
    </dl> The default is 0 (zero).<br/></td>
    </tr>
    </tbody>
    </table>

    

     

    The following code example shows how the context object is initialized to include qualifiers and exclude system properties.

    ```C++
    VARIANT vValue;
    IWbemContext *pContext = NULL;
    HRESULT hr = CoCreateInstance (CLSID_WbemContext, 
                           NULL, 
                           CLSCTX_INPROC_SERVER,
                           IID_IWbemContext, 
                           (void**) &pContext);
    if (FAILED(hr))
    {
      printf("Create context failed with %x\n", hr);
      return hr;
    }

    // Generate a <VALUE.OBJECTWITHLOCALPATH> element
    VariantInit(&vValue);
    vValue.vt = VT_I4;
    vValue.lVal = 2;
    pContext->SetValue(L"PathLevel", 0, &vValue);
    VariantClear(&vValue);

    // Include qualifiers
    VariantInit(&vValue);
    vValue.vt = VT_BOOL;
    vValue.boolVal = VARIANT_TRUE;
    pContext->SetValue(L"IncludeQualifiers", 0, &vValue);
    VariantClear(&vValue);

    // Exclude system properties
    VariantInit(&vValue);
    vValue.vt = VT_BOOL;
    vValue.boolVal = VARIANT_TRUE;
    pContext->SetValue(L"ExcludeSystemProperties", 0, &vValue);
    VariantClear(&vValue);
    ```

    

3.  Get a reference to the class or instance to encode in XML.

    After you have initialized COM and are connected to WMI, call [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) to retrieve a reference to the specified class or instance. If you used a BSTR to specify the class or instance, call [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free up the memory allocated by [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring).

    The following code example retrieves a reference to an [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) instance.

    ```C++
    HRESULT hr = NULL;
    IWbemClassObject *pClass = NULL;
    BSTR strObj = SysAllocString(L"Win32_LogicalDisk");

    hr = pConnection->GetObject(strObj, 
                                0, 
                                NULL, 
                                &pClass, 
                                NULL);

    SysFreeString(strObj);
    if (FAILED(hr))
    {
      printf("GetObject failed with %x\n",hr)
      return hr;
    }
    ```

    

4.  Create an [**IWbemObjectTextSrc**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc) object.

    After you have a reference to an object you must create the [**IWbemObjectTextSrc**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc) object with a call to [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance). The **IWbemObjectTextSrc** object is used to generate the actual XML text.

    The following code example shows how to create an [**IWbemObjectTextSrc**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc) object by calling [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance).

    ```C++
    HRESULT hr = NULL;
    IWbemObjectTextSrc *pSrc = NULL;

    hr = CoCreateInstance (CLSID_WbemObjectTextSrc, 
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           IID_IWbemObjectTextSrc, 
                           (void**) &pSrc);

    if (FAILED(hr))
    {
        printf("CoCreateInstance of IWbemObjectTextSrc failed %x\n",hr);
        return hr;
    }
    ```

    

5.  Invoke the [**IWbemObjectTextSrc.GetText**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjecttextsrc-gettext) method to get an XML representation of an object.

    After setting the context for the object's representation, getting a reference to the object, and creating an [**IWbemObjectTextSrc**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc) object, you are ready to generate an XML representation of the specified object by calling the [**IWbemObjectTextSrc.GetText**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjecttextsrc-gettext) method.

    The following C++ example code generates an XML representation of the object referenced by *pClass*. The XML representation is returned in *strText*. The third parameter of [**GetText**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc) specifies the text format to be used for the XML and must be either WMI\_OBJ\_TEXT\_CIM\_DTD\_2\_0 (0x1) or WMI\_OBJ\_TEXT\_WMI\_DTD\_2\_0 (0x2). For more information about these values, see [**IWbemObjectTextSrc::GetText**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjecttextsrc-gettext) Parameter Values.

    ```C++
    HRESULT hr = NULL;
    BSTR strText = NULL;
    hr = pSrc->GetText(0, 
                       pClass, 
                       WMI_OBJ_TEXT_CIM_DTD_2_0,
                       pContext, 
                       &strText);

    // Perform a task with strText
    SysFreeString(strText);

    if (FAILED(hr))
    {
      printf("GetText failed with %x\n", hr);
      return hr;
    }
    ```

    

The following C++ example code includes all of the steps in the previous procedure and encodes the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class in XML including class, property, and method qualifiers and excluding system properties.


```C++
// The following #define statement is needed so that 
// the proper values are loaded by the #include files.
#define _WIN32_WINNT 0x0500

#include <stdio.h>
#include <wbemcli.h>
#pragma comment(lib, "wbemuuid.lib")

// Initialize the context object
// ---------------------------------------------
void FillUpContext(IWbemContext *pContext)
{
  VARIANT vValue;

  // IncludeQualifiers
  VariantInit(&vValue);
  vValue.vt = VT_BOOL;
  vValue.boolVal = VARIANT_FALSE;
  pContext->SetValue(L"IncludeQualifiers", 0, &vValue);
  VariantClear(&vValue);

  VariantInit(&vValue);
  vValue.vt = VT_I4;
  vValue.lVal = 0;
  pContext->SetValue(L"PathLevel", 0, &vValue);
  VariantClear(&vValue);

  // ExcludeSystemProperties
  VariantInit(&vValue);
  vValue.vt = VT_BOOL;
  vValue.boolVal = VARIANT_TRUE;
  pContext->SetValue(L"ExcludeSystemProperties", 0, &vValue);
  VariantClear(&vValue);
}

// Main method ... drives the program
// ---------------------------------------------
int _cdecl main(int argc, char * argv[])
{
  BSTR strNs = NULL;
  BSTR strObj = NULL;
  BSTR strText = NULL;

  if(FAILED(CoInitialize(NULL)))
    return 1;
  HRESULT hr = E_FAIL;
  IWbemObjectTextSrc *pSrc = NULL;

  IWbemLocator *pL = NULL;
  if(SUCCEEDED(hr = CoCreateInstance (CLSID_WbemLocator, 
                                      NULL, 
                                      CLSCTX_INPROC_SERVER,
                                      IID_IWbemLocator, 
                                      (void**) &pL)))
  {
    // Create a context object
    IWbemContext *pContext = NULL;
    if(SUCCEEDED(hr = CoCreateInstance (CLSID_WbemContext, 
                                        NULL, 
                                        CLSCTX_INPROC_SERVER,
                                        IID_IWbemContext, 
                                        (void**) &pContext)))
    {
      FillUpContext(pContext);
      IWbemServices *pConnection = NULL;
      strNs = SysAllocString(L"root\\cimv2");
      strText = NULL;
      if(SUCCEEDED(hr = pL->ConnectServer(strNs, 
                                          NULL, 
                                          NULL, 
                                          NULL, 
                                          0, 
                                          NULL, 
                                          NULL, 
                                          &pConnection)))
      {
        IWbemClassObject *pClass = NULL;
        strObj = SysAllocString(L"Win32_LogicalDisk");

        if(SUCCEEDED(hr = CoCreateInstance (CLSID_WbemObjectTextSrc, 
                                            NULL,
                                            CLSCTX_INPROC_SERVER,
                                            IID_IWbemObjectTextSrc, 
                                            (void**) &pSrc)))
        {
          // Test for GetObject
          if(SUCCEEDED(hr = pConnection->GetObject(strObj, 
                                                   0, 
                                                   NULL, 
                                                   &pClass, 
                                                   NULL)))
          {
            if(SUCCEEDED(hr = pSrc->GetText(0, 
                                            pClass, 
                                            WMI_OBJ_TEXT_CIM_DTD_2_0,
                                            pContext, 
                                            &strText)))
            {
              printf("GETOBJECT SUCCEEDED\n");
              printf("==========================================\n");
              wprintf(strText);
              pContext->Release();
              pClass->Release();
            }
            else
            {
              printf("GetText failed with %x\n", hr);
              // Free up the object
              pContext->Release();
              pClass->Release();
            }
          }
          else
            printf("GetObject failed with %x\n", hr);
        }
        else
          printf("CoCreateInstance on WbemObjectTextSrc failed with %x\n", hr);
      }
      else
        printf("ConnectServer on root\\cimv2 failed with %x\n", hr);
    }
    else
      printf("CoCreateInstance on Context failed with %x\n", hr);
  }
  else
    printf("CoCreateInstance on Locator failed with %x\n", hr);

// Clean up memory
  if (strNs != NULL)
    SysFreeString(strNs);
  if (strObj != NULL)
    SysFreeString(strObj);
  if (strText != NULL)
    SysFreeString(strText);
  if (pSrc != NULL)
    pSrc->Release();
  if (pL != NULL)
    pL->Release();
  return 0;
}
```



## Encode an Object Using VBScript

<span id="to_encode_an_object_in_xml_using_vbscript"></span><span id="TO_ENCODE_AN_OBJECT_IN_XML_USING_VBSCRIPT"></span>

The following procedure describes how to encode an object in XML using VBScript.

**To encode an object in XML using VBScript**

1.  Optionally, create an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object and initialize it so as to set the context values required for the XML representation.

    The following code example shows how the values instruct the XML encoder to generate a <VALUE.OBJECTWITHLOCALPATH> element, including all of the qualifiers and excluding system properties when it constructs the XML representation of the object.

    ```VB
    ' Create an optional SWbemNamedValueSet object
    set context = CreateObject("wbemscripting.SWbemNamedValueSet")

    ' Initialize the value set object to set the context
    ' Generate a <VALUE.OBJECTWITHLOCALPATH> element
    context.add "PathLevel", 2 
    context.add "IncludeQualifiers", true 
    context.add "ExcludeSystemProperties", true '
    ```

    

2.  Retrieve an instance of the object or class to represent in XML.

    The following code example retrieves an instance of the object.

    ```VB
    ' Retrieve the object/class to be represented in XML
    set myObj = GetObject("winmgmts:\\.\root\cimv2:win32_LogicalDisk")
    ```

    

3.  Invoke the [**GetText\_**](swbemobjectex-gettext-.md) method of the instance created in the preceding step, using 1 as the parameter to specify the text format that corresponds to CIM DTD version 2.0, or 2 to specify the text format that corresponds to WMI DTD version 2.0. If you created the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object in Step 1, include it in the parameter list as the third parameter.

    The following code example shows how to invoke the [**GetText\_**](swbemobjectex-gettext-.md) method of the instance.

    ```VB
    ' Get the XML representation of the object
    strText = myObj.GetText_(2,,context)

    ' If you have not used a SWbemNamedValueSet object
    ' enter the following line.
    strText = myObj.GetText_(2)
    ```

    

4.  Optionally, validate that the XML generated in Step 3 is well-formed XML, by creating and initializing an XML Document Object Model (DOM) object and then load the XML text into it.

    The following code example shows how to create and initialize an XML DOM object and load the XML text into it.

    ```VB
    ' Create an XMLDOM object
    set xml = CreateObject("Microsoft.xmldom")

    ' Initialize the XMLDOM object so results are returned synchronously
    xml.async = false

    ' Load the XML into the XMLDOM object
    xml.loadxml strText
    ```

    

5.  Output the XML representation of the object.

    The following code example shows how to use wscript to output the XML.

    ```VB
    wscript.echo strText
    ```

    

    If you chose to use XML DOM to verify that the XML generated is well-formed, replace the previous line with the following.

    ```VB
    wscript.echo xml.xml
    ```

    

The following VBScript code example includes all of the steps in the preceding procedure and encodes the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class in XML, including class, property, and method qualifiers and excluding system properties.


```VB
' Create optional SWbemNamedValueSet object
set context = CreateObject("Wbemscripting.SWbemNamedValueSet")

' Initialize the context object
context.add "PathLevel", 2
context.add "IncludeQualifiers", true
context.add "ExcludeSystemProperties", true

' Retrieve the object/class to be represented in XML
set myObj = GetObject("winmgmts:\\.\root\cimv2:Win32_LogicalDisk")

' Get the XML representation of the object
strText = myObj.GetText_(2,,context)
' If you have not used a SWbemNamedValueSet object 
'   use the following line
'   strText = myObj.GetText(2)

' Print the XML representation
wscript.echo strText

' If you choose to use the XML DOM to verify 
'   that the XML generated is well-formed, replace the last
'   line in the above code example with the following lines:

' Create an XMLDOM object
set xml = CreateObject("Microsoft.xmldom")

' Initialize the XMLDOM object so results are 
'   returned synchronously
xml.async = false

' Load the XML into the XMLDOM object
xml.loadxml strText

' Print the XML representation
wscript.echo xml.xml
```



## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

