---
title: Retrieving Device Attributes
description: Retrieving Device Attributes
ms.assetid: c553d495-d8fc-4483-a3dc-6679c6b9d1f1
keywords:
- Windows Media Player,portable devices
- Windows Media Player object model,portable devices
- object model,portable devices
- Windows Media Player ActiveX control,portable devices
- ActiveX control,portable devices
- Windows Media Player Mobile ActiveX control,portable devices
- Windows Media Player Mobile,portable devices
- portable devices,retrieving attributes
- attributes,portable devices
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Device Attributes

Windows Media Player stores information about devices that have connected to the Player. Some attributes are available by calling individual methods of **IWMPSyncDevice**, some can be retrieved by using **IWMPSyncDevice::getItemInfo**, and some can be retrieved by using either technique.

The following example code fills a list box control with the available attributes for the specified device. The first part of the function retrieves properties available by using specific methods. The second part of the function retrieves attribute values by using **IWMPSyncDevice::getItemInfo**. The function parameter, *lIndex*, is the index to the device in your custom device array pointed to by m\_ppWMPDevices.


```C++
STDMETHODIMP CMainDlg::ShowDeviceAttributes(long lIndex)
{
    HRESULT hr = S_OK;

    if(!m_ppWMPDevices)
        return S_FALSE;

    // Array of attribute names for devices.
    const TCHAR *szDeviceAttributeNames[16] = {
    _T("Connected"),
    _T("FreeSpace"),
    _T("FriendlyName"),
    _T("LastSyncErrorCount"),
    _T("LastSyncNoFitCount"),
    _T("LastSyncTime"),
    _T("Name"),
    _T("SerialNumber"),
    _T("SupportsAudio"),
    _T("SupportsPhoto"),
    _T("SupportsVideo"),
    _T("SyncIndex"),
    _T("SyncItemCount"),
    _T("SyncPercentComplete"),
    _T("SyncRelationship"),
    _T("TotalSpace")};
    
    // Array of device status strings.
    static const TCHAR *szDeviceStatus[6] = {
    _T("Unknown"),
    _T("Partnership exists"),
    _T("Partnership declined by the user"),
    _T("Partnership with another computer or user"),
    _T("Device only supports manual transfer"),
    _T("New device")};

    // Handle to the list box that displays the information.
    HWND hwndStats = GetDlgItem(IDC_STATS);
    CComBSTR bstrStatistics;  // Contains the display string for each property.
    CComBSTR bstrTemp; // Contains the retrieved value for each property.
    // Retrieve a pointer to the current device.
    CComPtr<IWMPSyncDevice> spDevice(m_ppWMPDevices[GetSelectedDeviceIndex()]);
    VARIANT_BOOL vbIsConnected = VARIANT_FALSE;
    WMPDeviceStatus  wmpDS = wmpdsUnknown;
    
    SendMessage(hwndStats, LB_RESETCONTENT, 0, 0);

    if(NULL == spDevice.p)
    {
        return E_POINTER;
    }
 
    // Status
    spDevice->get_status(&wmpDS);
    bstrStatistics = "Status: ";
    bstrTemp = szDeviceStatus[wmpDS];
    bstrStatistics += bstrTemp;
    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics)); 
    bstrTemp.Empty();
    
    // Connected?
    spDevice->get_connected(&vbIsConnected);
    bstrStatistics = "Connected: ";
    bstrTemp = (vbIsConnected == VARIANT_TRUE)?"True":"False";
    bstrStatistics += bstrTemp;
    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics));
    bstrTemp.Empty();
    
    // Device ID
    spDevice->get_deviceId(&bstrTemp);
    bstrStatistics = "Device ID: ";
    bstrStatistics += bstrTemp;

    // Calculate the list box width based on text metrics.
    // This assumes Device ID is likely to be the longest string.
    HDC hDC = GetDC();
    SIZE sizeText = {0, 0};
    GetTextExtentPoint32(hDC, (LPCTSTR)COLE2T(bstrStatistics), bstrStatistics.Length(), &sizeText);
    ReleaseDC(hDC);

    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics)); 
    SendMessage(hwndStats, LB_SETHORIZONTALEXTENT, sizeText.cx, 0);
    bstrTemp.Empty();

    // Friendly name
    spDevice->get_friendlyName(&bstrTemp);
    bstrStatistics = "Friendly name: ";
    bstrStatistics += bstrTemp;
    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics)); 
    bstrTemp.Empty();

    // Skip a line and label the getItemInfo attributes.
    bstrStatistics = "";
    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics)); 
    bstrStatistics = "--getItemInfo Attributes--";
    SendMessage(hwndStats, LB_ADDSTRING, 0,(LPARAM)(LPCTSTR)COLE2T(bstrStatistics)); 

    // Show the getItemInfo attributes.
    int iArrayBound = sizeof szDeviceAttributeNames / sizeof szDeviceAttributeNames[0];
    for(int i = 0; i < iArrayBound; i++)
    {
        CComBSTR bstrName(szDeviceAttributeNames[i]);
        CComBSTR bstrVal;
        CComBSTR bstrDisplayString;
       
        hr = spDevice->getItemInfo(bstrName, &bstrVal);
  
        if(FAILED(hr))
        {
             bstrVal.Append("Error");
        }  
        
        bstrName.Append(L": ");
        bstrDisplayString.AppendBSTR(bstrName);
        bstrDisplayString += bstrVal;  
 
        SendMessage(hwndStats, LB_ADDSTRING, 0, (LPARAM)(LPCTSTR)COLE2T(bstrDisplayString));
    }    

    return hr;
}
```



## Related topics

<dl> <dt>

[**Enumerating Devices**](enumerating-devices.md)
</dt> <dt>

[**IWMPSyncDevice Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice)
</dt> <dt>

[**IWMPSyncDevice::getItemInfo**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-getiteminfo)
</dt> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




