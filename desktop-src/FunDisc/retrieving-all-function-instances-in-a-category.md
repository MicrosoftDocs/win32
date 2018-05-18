---
Description: 'The following topic describes how to retrieve function instances using Function Discovery APIs.'
ms.assetid: '08e39100-bfc0-4e69-b311-451e144cdb90'
title: Retrieving All Function Instances in a Category
---

# Retrieving All Function Instances in a Category

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The following topic describes how to retrieve function instances using Function Discovery APIs.

To get a collection of function instances, use the [**IFunctionDiscovery::GetInstanceCollection**](ifunctiondiscovery-getinstancecollection-method.md) method. To get a specified function instance and its index from the collection, use the [**IFunctionInstanceCollection::Get**](ifunctioninstancecollection-get.md) method. To get each function instance in the collection in order, use the [**IFunctionInstanceCollection::Item**](ifunctioninstancecollection-item-method.md) method.

If the [**GetInstanceCollection**](ifunctiondiscovery-getinstancecollection-method.md) method succeeds but no function instances were found that matched the query parameters, then **GetInstanceCollection** returns **S\_OK**, *ppFunctionInstanceCollection* points to an empty collection, and the collection's [**GetCount**](ifunctioninstancecollection-getcount-method.md) method returns 0.

> [!Note]  
> Function Discovery network providers, such as the SSDP Provider, the WSD Provider, only return instances through the [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) interface.

 

The following code snippet demonstrates how to get an instance from the collection using the [**IFunctionInstanceCollection::Item**](ifunctioninstancecollection-item-method.md) method. Implement the **DisplayInstance** function to display the returned function instance.


```C++
IFunctionDiscovery *pIFunDisc;
IFunctionInstanceCollectionQuery *pIFunInstCollectionQuery;
IFunctionInstanceCollection *pIFunInstCollection;
IFunctionInstance *pIFunInst;
BSTR _bstrCategory, _bstrSubCategory;
BOOL bRecursive;
DWORD dwCount;

// some initialization code omitted here for brevity
if ( S_OK == hr ) 
{
    hr = pIFunDisc->CreateInstanceCollectionQuery( _bstrCategory, 
                                                   _bstrSubCategory, 
                                                   bRecursive, 
                                                   NULL, 
                                                   NULL, 
                                                   &amp;pIFunInstCollectionQuery );
    if ( S_OK == hr )
    { 
        hr = pIFunInstCollectionQuery->Execute( &amp;pIFunInstCollection );
        if ( S_OK == hr )
        {
            hr = pIFunInstCollection->GetCount( &amp;dwCount );
            for ( DWORD dwItem = 0; S_OK == hr &amp;&amp; dwItem < dwCount; dwItem++ )
            {
                hr = pIFunInstCollection->Item( dwItem, &amp;pIFunInst );
                if ( S_OK == hr )
                {
                    hr = DisplayInstance( pIFunInst );    // Implement DisplayInstance before using this sample code.
                                                        
                    pIFunInst->Release();
                }
            }
            pIFunInstCollection->Release();
        }
        pIFunInstCollectionQuery->Release();
    }
}

// cleanup code omitted here for brevity

```



The [**IFunctionInstanceQuery**](ifunctioninstancequery.md) interface implements the asynchronous query for a function instance based on category and subcategory. It is returned when [**IFunctionDiscovery::CreateInstanceQuery**](ifunctiondiscovery-createinstancequery-method.md) is invoked by the client program. Set interface constraints using [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) to filter on multiple interfaces at one time.

> [!Note]  
> The [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) method must be invoked by the client program before any data can be retrieved from the query object.

 

 

 



