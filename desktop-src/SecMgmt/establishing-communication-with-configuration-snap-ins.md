---
Description: 'After your attachment snap-in extension has added itself to the Services node, it should establish communication with the Security Configuration snap-in.'
ms.assetid: '68a0e5a7-938f-45b7-90a3-8f35e5e6bbfb'
title: 'Establishing Communication with Configuration Snap-ins'
---

# Establishing Communication with Configuration Snap-ins

After your attachment snap-in extension has added itself to the Services node, it should establish communication with the Security Configuration snap-in. This is necessary because the attachment snap-in extension gets its data, as well as any changes made by the user, from the Security Configuration snap-in. This can be done as described in the following procedure.

**To establish communication with the Security Configuration snap-ins**

1.  Obtain the configuration file name using the CCF\_SCESVC\_ATTACHMENT clipboard format, which returns the configuration file name as a **PWSTR**.

    If the attachment is inserted under a configuration type node, the attachment needs to know which configuration it is. (It communicates this information to the Security Configuration snap-ins during interface initialization.) In this case, use the following code.

    ```C++
    PWSTR * TemplateName = ExtractTemplateFromDataObject(lpDataObject);
    ```

    

2.  Set up the context with the Security Configuration snap-ins. After the configuration name is known, or if the service node is an analysis node, the attachment snap-in extension must call [**ISceSvcAttachmentData::Initialize**](iscesvcattachmentdata-initialize.md) to set up the context, as shown in the following example.

    ```C++
    LPSCESVCATTACHMENTPERSISTINFO pSceInfo;

        HRESULT hr = ((LPSCESVCATTACHMENTPERSISTINFO)this)->
                QueryInterface(IID_ISceSvcAttachmentPersistInfo,
                (void**)&amp;pSceInfo);

        if ( SUCCEEDED(hr) )
        {

            hr = m_pSceData->Initialize(strServiceName, TemplateName,
                    pSceInfo, &amp;ThisHandle);
            // Continue processing (not shown).
        }
    ```

    

> [!Note]  
> When you have finished using the handle returned by [**ISceSvcAttachmentData::Initialize**](iscesvcattachmentdata-initialize.md), close the handle by calling the [**ISceSvcAttachmentData::CloseHandle**](iscesvcattachmentdata-closehandle.md) function. This is typically done when the user closes the MMC console.

 

 

 



