---
Description: 'If the property that you retrieve from a rowset or rowset enumerator does not contain a value, the property is null.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '98ac7579-1ec3-4e03-869a-ab6fe14ea422'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Checking for Null Property Values
---

# Checking for Null Property Values

If the property that you retrieve from a rowset or rowset enumerator does not contain a value, the property is null. If you try to access the property value without first testing for null, you will receive a NullReferenceException exception. The following examples show possible ways to test for a null property value when accessing properties in a rowset.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Checking_for_NULL_Property_Values
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();

            try
            {
                scheduler.Connect("localhost");

                CauseAnException(scheduler);
                CheckForNullPropertyValue(scheduler);
                UseErrorPropertyToCheckForNull(scheduler);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }


        // Shows how not to access properties from a rowset.
        private static void CauseAnException(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rows = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();
            StoreProperty property = null;

            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.State);
            properties.Add(JobPropertyIds.TotalCpuTime);
            properties.Add(JobPropertyIds.TotalKernelTime);
            properties.Add(JobPropertyIds.TotalUserTime);

            // Get the specified job. Specify a job that is in the configuring state for this test.
            filters.Add(FilterOperator.Equal, JobPropertyIds.Id, 1);

            using (rows = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                try
                {
                    PropertyRowSet rowset = rows.GetRows(1);

                    if (0 == rowset.Length)
                        Console.WriteLine("Job not found");
                    else
                    {
                        // Get the job from the rowset.
                        PropertyRow row = rowset.Rows[0];

                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        property = row[JobPropertyIds.State];
                        Console.WriteLine("State: {0}", (null != property) ? property.Value : "");

                        property = row[JobPropertyIds.TotalCpuTime];
                        Console.WriteLine("TotalCpuTime: {0}", (null != property) ? property.Value : "");

                        // Both of the next statements will throw a NullReferenceException if the 
                        // job has not run. 
                        Console.WriteLine("TotalKernelTime: {0}", row[JobPropertyIds.TotalKernelTime].Value);

                        property = row[JobPropertyIds.TotalUserTime];
                        Console.WriteLine("TotalUserTime: {0}", property.Value);
                    }
                }
                catch (NullReferenceException nullRef)
                {
                    Console.WriteLine(nullRef.Message);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }

        // Shows one option for accessing the properties of a rowset.
        private static void CheckForNullPropertyValue(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rows = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();
            StoreProperty property = null;

            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.State);
            properties.Add(JobPropertyIds.TotalCpuTime);
            properties.Add(JobPropertyIds.TotalKernelTime);
            properties.Add(JobPropertyIds.TotalUserTime);

            // Get the specified job. Specify a job that is in the configuring state for this test.
            filters.Add(FilterOperator.Equal, JobPropertyIds.Id, 1);

            using (rows = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                try
                {
                    PropertyRowSet rowset = rows.GetRows(1);

                    if (0 == rowset.Length)
                        Console.WriteLine("Job not found");
                    else
                    {
                        // Get the job from the rowset.
                        PropertyRow row = rowset.Rows[0];

                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        // Check if property is null before accessing its value.
                        property = row[JobPropertyIds.State];
                        Console.WriteLine("State: {0}", (null != property) ? property.Value : "");

                        property = row[JobPropertyIds.TotalCpuTime];
                        Console.WriteLine("TotalCpuTime: {0}", (null != property) ? property.Value : "");

                        property = row[JobPropertyIds.TotalKernelTime];
                        Console.WriteLine("TotalKernelTime: {0}", (null != property) ? property.Value : "");

                        property = row[JobPropertyIds.TotalUserTime];
                        Console.WriteLine("TotalUserTime: {0}", (null != property) ? property.Value : "");
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }


        // Shows another option for accessing the properties of a rowset.
        private static void UseErrorPropertyToCheckForNull(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rows = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();
            StoreProperty property = null;

            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.State);
            properties.Add(JobPropertyIds.TotalCpuTime);
            properties.Add(JobPropertyIds.TotalKernelTime);
            properties.Add(JobPropertyIds.TotalUserTime);

            // Get the specified job. Specify a job that is in the configuring state for this test.
            filters.Add(FilterOperator.Equal, JobPropertyIds.Id, 1);

            using (rows = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                try
                {
                    PropertyRowSet rowset = rows.GetRows(1);

                    if (0 == rowset.Length)
                        Console.WriteLine("Job not found");
                    else
                    {
                        // Get the job from the rowset.
                        PropertyRow row = rowset.Rows[0];

                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        property = row[JobPropertyIds.State];
                        Console.WriteLine("State: {0}", (null != property) ? property.Value : "");


                        // With this option, you must use a zero-based index to index the 
                        // property instead of using the property identifier to index the property.
                        // The index is based on the position in which you insert the property 
                        // identifier into your IPropertyIdCollection collection.

                        // For each property that you retrieve, the store returns two values. 
                        // The first is the property value and the second is the error value 
                        // (which indicates why the call did not return the property value). 
                        // If you use the property identifier to index the value, you receive 
                        // the property value. If you use the zero-based index to retrieve the 
                        // property, you receive either the property value, if it was returned, 
                        // or the PropertyError value. 

                        property = row[JobPropertyIds.TotalCpuTime];
                        if (null == property)
                            Console.WriteLine("TotalCpuTime: " + row[2].Value);
                        else
                            Console.WriteLine("TotalCpuTime: " + property.Value);

                        // If you do not need to know that the property was not 
                        // retrieved, you can simply use the index to access the 
                        // value.
                        Console.WriteLine("TotalKernelTime: " + row[3].Value);
                        Console.WriteLine("TotalUserTime: " + row[4].Value);
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }

    }
}
```



 

 



