---
Description: 'To access the cluster, call the ICluster::Connect method and pass the computer name of the cluster's head node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e4652c77-bd67-4d16-81dd-9cecf6722cec'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Connecting to the Cluster
---

# Connecting to the Cluster

To access the cluster, call the [**ICluster::Connect**](icluster-connect.md) method and pass the computer name of the cluster's head node. If you are logged on to the head node, you can use "localhost" as the name; otherwise, you must specify the name of the head node. The name can be the head node's computer name or its fully qualified domain name.

The following C++ example shows how to connect to a cluster. The example assumes that `pCluster` points to a valid [**ICluster**](icluster.md) instance.


```C++
  if (ConnectToServer(pCluster, L"localhost"))
  {
    // Do something
  }


// Connect to the specified cluster. Set pClusterName to the name of 
// the cluster's head node.
BOOL ConnectToServer(ICluster* pCluster, LPWSTR pClusterName)
{
  HRESULT hr = S_OK;

  // Connect to the server. 
  hr = pCluster->Connect(_bstr_t(pClusterName));
  if (FAILED(hr))
  {
    wprintf(L"Failed to connect to cluster, %s.\n", pClusterName);
    return FALSE;
  }

  wprintf(L"Connected to cluster, %s.\n", pClusterName);

  return TRUE;
}
```



The following C# example shows how to connect to a cluster. The example assumes that `cluster` points to a valid **ICluster** instance and that the value of `nodeName` is the name of the head node or "localhost".


```CSharp
    try
    {
        cluster.Connect(nodeName);
    }
    catch
    {
        string message = "Failed to connect to the cluster, " + nodeName + ".\n\n";

        message = message + cluster.ErrorMessage + ".";

        MessageBox.Show(message, "Connection failure");
    }
```



If you do not know the names of the head nodes in a domain, you can use Active Directory to search for the names, as shown in the following example.


```C++
// Link to Activeds.lib and Adsiid.lib

#include <vector>
#include <activeds.h>

  std::vector<LPWSTR> pHeadNodes;
  DWORD size = 0;

  FindConnectionPoints(pHeadNodes);

  if (!pHeadNodes.empty())
  {
    size = (DWORD) pHeadNodes.size();
    wprintf(L"Found the following %d head nodes.\n", size);

    for (DWORD i=0; i<size; i++)
    {
      wprintf(L"%s\n", pHeadNodes[i]);
    }

    ClearConnectionPoints(pHeadNodes);
  }


// Use Active Directory to find the head nodes of the compute clusters 
// in a domain.
void FindConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes)
{
  HRESULT hr = S_OK;
  IADs* pObject = NULL;
  IDirectorySearch* pSearch = NULL;
  ADS_SEARCH_HANDLE hSearch;
  WCHAR szPath[MAX_PATH];
  VARIANT var;
  LPWSTR pNodeName = NULL;
  BOOL fAllocationError = FALSE;
  size_t length = 0;


  // Bind to LDAP://rootDSE.
  hr = ADsOpenObject(L"LDAP://rootDSE",
                     NULL,
                     NULL,
                     ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                     IID_IADs,
                     (void**)&amp;pObject);
  if (FAILED(hr))
  {
    wprintf(L"Cannot execute query. Cannot bind to LDAP://rootDSE.\n");
    return;
  }

  hr = pObject->Get(_bstr_t("defaultNamingContext"), &amp;var);
  if (SUCCEEDED(hr))
  {
    // Build path to the domain container.
    StringCchPrintf(szPath, MAX_PATH, L"LDAP://");
    StringCchCatN(szPath, MAX_PATH, var.bstrVal, MAX_PATH - wcslen(szPath));
    VariantClear(&amp;var);

    // Get the DirectorySearch object used to search Active Directory.
    hr = ADsOpenObject(szPath,
                       NULL,
                       NULL,
                       ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                       IID_IDirectorySearch,
                       (void**)&amp;pSearch);
    if (FAILED(hr))
    {
      wprintf(L"Failed to create DirectorySearch object, 0x%x.\n", hr);
    }
    else
    {
      // This attribute contains the FQDN of the head node.
      LPWSTR pszAttrs[] = { L"servicednsname" }; 
      DWORD dwCount = sizeof(pszAttrs)/sizeof(LPWSTR);
      ADS_SEARCH_COLUMN DnsNameColumn;

      // Search for the service connection points. 
      hr = pSearch->ExecuteSearch(L"(&amp;(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster))",
                                  pszAttrs, 
                                  dwCount, 
                                  &amp;hSearch);
      if (FAILED(hr))
      {
        wprintf(L"pSearch->ExecuteSearch failed, 0x%x\n", hr);
      }
      else
      {
        hr = pSearch->GetFirstRow(hSearch);
        if (SUCCEEDED(hr))
        {
          while( hr != S_ADS_NOMORE_ROWS &amp;&amp; !fAllocationError)
          {
            hr = pSearch->GetColumn(hSearch, L"servicednsname", &amp;DnsNameColumn );
            if ( SUCCEEDED(hr) )
            {
              length = wcslen(DnsNameColumn.pADsValues->CaseIgnoreString) + 1;
              pNodeName = (LPWSTR) malloc(length * sizeof(WCHAR));
              if (pNodeName)
              {
                StringCchCopy(pNodeName, length+1, DnsNameColumn.pADsValues->CaseIgnoreString);
                pHeadNodes.push_back( pNodeName );
              }
              else
              {
                wprintf(L"Failed to allocate memory for node name.\n");
                pSearch->FreeColumn( &amp;DnsNameColumn );
                fAllocationError = TRUE;
                ClearConnectionPoints(pHeadNodes);
                continue;
              }

              pSearch->FreeColumn( &amp;DnsNameColumn );
            }

            // Get the next row.
            hr = pSearch->GetNextRow( hSearch);
          }
        }
   
        pSearch->CloseSearchHandle(hSearch);
      }

      pSearch->Release();
    }
  }

  pObject->Release();
}


// Free the node names in the vector and clear the vector.
void ClearConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes)
{
  DWORD size = 0;

  if (!pHeadNodes.empty())
  {
    size = (DWORD) pHeadNodes.size();

    for (DWORD i=0; i<size; i++)
    {
      if (pHeadNodes[i])
        free(pHeadNodes[i]);
    }

    pHeadNodes.clear();
  }
}
```




```CSharp
        // Reference System.DirectoryServices;
        private void LoadHeadNodes()
        {
            string dnsName;

            // Bind to current domain
            searchRoot = new DirectoryEntry("LDAP://rootDSE");
            domain = new DirectoryEntry("LDAP://" + searchRoot.Properties["defaultNamingContext"][0]);
            searchRoot.Dispose();

            string domainName = domain.Name.Substring(3);  // DC=name
            lblSelectDomain.Text = "Select the cluster to connect to from the " + domainName + " domain.";

            // Search for head nodes in current domain
            string[] propsToLoad = new string[] { "servicednsname" };
            string filterForAllHeadNodes = "(&amp;(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster))";
            searcher = new DirectorySearcher(domain, filterForAllHeadNodes, propsToLoad);

            SearchResultCollection results = searcher.FindAll();

            cbHeadNodes.BeginUpdate();

            // Enumerate head nodes and load list
            foreach (SearchResult result in results)
            {
                int index = 0;

                dnsName = (string)result.Properties["servicednsname"][0];

                // Get the name from the fully qualified path, if qualified.
                if ((index = dnsName.IndexOf('.')) > 0)
                    cbHeadNodes.Items.Add(dnsName.Substring(0, index));
                else
                    cbHeadNodes.Items.Add(dnsName);
            }

            results.Dispose();

            // Get name of local computer
            string localHost = System.Net.Dns.GetHostEntry("LocalHost").HostName;
            string filterForLocalHeadNode = "(&amp;(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster)(servicednsname=" + localHost + "))";

            // Change filter string filter on servicednsname too
            searcher.Filter = filterForLocalHeadNode;

            results = searcher.FindAll();

            // If the local computer is a head node, make its entry the selected item.
            if (results.Count > 0)
            {
                dnsName = (string)results[0].Properties["servicednsname"][0];
                cbHeadNodes.SelectedItem = dnsName.Substring(0, dnsName.IndexOf('.'));
            }
            else
            {
                cbHeadNodes.SelectedIndex = 0;
            }

            cbHeadNodes.EndUpdate();

            results.Dispose();
            domain.Dispose();
        }

```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



