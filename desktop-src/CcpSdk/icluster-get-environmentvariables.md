---
Description: 'Retrieves the cluster-wide environment variables. The variables are available to all tasks on all nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7f5174ae-eb4d-4231-b68c-7866e10c6672'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_EnvironmentVariables method'
---

# ICluster::get\_EnvironmentVariables method

Retrieves the cluster-wide environment variables. The variables are available to all tasks on all nodes.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains the collection of environment variables. The variant type of each item in the collection is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

To set a cluster-wide environment variable, call the [**ICluster::SetEnvironmentVariable**](icluster-setenvironmentvariable.md) method. To set an environment variable that is available to a specific task, call the [**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md) method.

## Examples

The following example shows how to call this method. The example assumes the *pCluster* parameter points to a valid [**ICluster**](icluster.md) interface.


```C++
void ListClusterEnvironmentVariables(ICluster* pCluster)
{
  HRESULT hr = S_OK;
  INameValueCollection* pCollection = NULL;
  INameValue* pVariable = NULL;
  IEnumVARIANT* pVariables = NULL;
  long count = 0;
  BSTR bstrClusterName = NULL;
  BSTR bstrVariableName = NULL;
  BSTR bstrVariableValue = NULL;
  VARIANT var;

  hr = pCluster->get_EnvironmentVariables(&amp;pCollection);
  if (FAILED(hr))
  {
    wprintf(L"pCluster->get_EnvironmentVariables failed.\n");
    return;
  }

  hr = pCollection->GetEnumerator(&amp;pVariables);
  if (FAILED(hr))
  {
    wprintf(L"pCollection->GetEnumerator failed.\n");
    goto cleanup;
  }

  hr = pCollection->get_Count(&amp;count);
  if (FAILED(hr))
  {
    wprintf(L"pCollection->get_Count failed.\n");
    goto cleanup;
  }

  hr = pCluster->get_Name(&amp;bstrClusterName);
  if (FAILED(hr))
  {
    wprintf(L"pCluster->get_Name failed.\n");
    goto cleanup;
  }

  wprintf(L"\nThe following lists the %d environment variable for the cluster, %s:\n", count, bstrClusterName);

  VariantInit(&amp;var);

  while (hr = pVariables->Next(1, &amp;var, NULL) == S_OK)
  {
    var.pdispVal->QueryInterface(IID_INameValue, reinterpret_cast<void **> (&amp;pVariable));

    hr = pVariable->get_Name(&amp;bstrVariableName);
    if (SUCCEEDED(hr))
    {
      wprintf(L"\nName: %s\n", bstrVariableName);
      SysFreeString(bstrVariableName);

      hr = pVariable->get_Value(&amp;bstrVariableValue);
      if (SUCCEEDED(hr))
      {
        wprintf(L"Value: %s\n", bstrVariableValue);
        SysFreeString(bstrVariableValue);
      }
      else
      {
        wprintf(L"Failed to get variable value.\n");
      }
    }
    else
    {
      wprintf(L"Failed to get variable name.\n");
    }

    pVariable->Release();
    pVariable = NULL;

    VariantClear(&amp;var);
  }

cleanup:

  if (pCollection)
    pCollection->Release();

  if (pVariables)
    pVariables->Release();

  SysFreeString(bstrClusterName);

  return;
}
```



## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md)
</dt> </dl>

 

 




