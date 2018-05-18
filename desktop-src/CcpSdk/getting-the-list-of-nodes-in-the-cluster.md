---
Description: 'The following example shows how to list the compute nodes of a cluster and get information about them, such as the amount of memory and number of processors.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '46f508fb-7423-4a08-8831-fbdb31d989a0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Getting the List of Nodes in the Cluster
---

# Getting the List of Nodes in the Cluster

The following example shows how to list the compute nodes of a cluster and get information about them, such as the amount of memory and number of processors.


```C++
WCHAR *NodeStatusStrings[] = { L"Ready", L"Paused", 
                               L"Unreachable", L"Pending"
                             };


// Get the collection of compute nodes and enumerate the
// list. For each node, print details about the node.
void ListNodes(ICluster* pCluster)
{
  HRESULT hr = S_OK;
  IClusterEnumerable* pNodesCollection = NULL;
  IEnumVARIANT* pNodes = NULL;
  INode* pNode = NULL;
  BSTR bstrMessage = NULL;
  VARIANT var;


  // Get the collection of nodes.
  hr = pCluster->get_ComputeNodes(&amp;pNodesCollection);
  if (FAILED(hr))
  {
    wprintf(L"pCluster->get_ComputeNodes failed.\n");
    hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
    wprintf(L"%s.\n", bstrMessage);
    SysFreeString(bstrMessage);
    return;
  }

  // Get the enumerator used to iterate through the collection.
  hr = pNodesCollection->GetEnumerator(&amp;pNodes);
  if (SUCCEEDED(hr))
  {
    VariantInit(&amp;var);

    // Loop through the collection.
    while (hr = pNodes->Next(1, &amp;var, NULL) == S_OK)
    {
      var.pdispVal->QueryInterface(IID_INode, reinterpret_cast<void **> (&amp;pNode));

      DisplayNodeProperties(pNode);
      pNode->Release();

      VariantClear(&amp;var);
    }

    pNodes->Release();
  }
  else
  {
    wprintf(L"pNodesCollection->GetEnumerator failed.\n");
    hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
    wprintf(L"%s.\n", bstrMessage);
    SysFreeString(bstrMessage);
  }

  pNodesCollection->Release();
  return;
}


// Display the properties of a compute cluster node.
void DisplayNodeProperties(INode* pNode)
{
  HRESULT hr = S_OK;
  BOOL fDisplayProperties = TRUE;
  BSTR bstrNodeName = NULL;
  BSTR bstrArchitecture = NULL;
  long Memory = 0;
  long IdleProcessors = 0;
  long Processors = 0;
  long Speed = 0;
  NodeStatus Status;


  hr = pNode->get_Name(&amp;bstrNodeName);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_Name failed.\n");
    goto cleanup;
  }

  hr = pNode->get_ProcessorArchitecture(&amp;bstrArchitecture);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_ProcessorArchitecture failed.\n");
    goto cleanup;
  }

  hr = pNode->get_Memory(&amp;Memory);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_Memory failed.\n");
    goto cleanup;
  }

  hr = pNode->get_NumberOfIdleProcessors(&amp;IdleProcessors);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_NumberOfIdleProcessors failed.\n");
    goto cleanup;
  }

  hr = pNode->get_NumberOfProcessors(&amp;Processors);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_NumberOfProcessors failed.\n");
    goto cleanup;
  }

  hr = pNode->get_ProcessorSpeed(&amp;Speed);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_ProcessorSpeed failed.\n");
    goto cleanup;
  }

  hr = pNode->get_Status(&amp;Status);
  if (FAILED(hr))
  {
    wprintf(L"pNode->get_Status failed.\n");
    goto cleanup;
  }

  wprintf(L"\nNode name: %s\n", bstrNodeName);
  wprintf(L"Architecture: %s\n", bstrArchitecture);
  wprintf(L"Number of processors: %d (of which %d are idle)\n", 
          Processors, IdleProcessors);
  wprintf(L"Processor speed: %.3fGHz\n", Speed/1000.0);
  wprintf(L"Status: %s\n", NodeStatusStrings[Status]);
    
cleanup:

  SysFreeString(bstrNodeName);
  SysFreeString(bstrArchitecture);

}
```




```CSharp
        public static IClusterEnumerable clusterNodes;

        private void LoadComputeNodesList()
        {
            if (null == clusterNodes)
                clusterNodes = cluster.ComputeNodes;

            foreach (INode node in clusterNodes)
            {
                ListViewItem lvi = new ListViewItem(new string[] {
                        node.Name, 
                        node.Status.ToString(), 
                        String.Format("{0} GB", node.Memory / 1000),  
                        node.NumberOfProcessors.ToString(),
                        String.Format("{0:F1} GHz", node.ProcessorSpeed / 1000.0)
                    });

                lvi.Tag = node.Status;
                listComputeNodes.Items.Add(lvi);
            }
        }
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



