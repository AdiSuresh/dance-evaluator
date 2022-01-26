using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dance : MonoBehaviour
{
    int size = 
    public GameObject Armature;
    public GameObject[] Array;


    // Start is called before the first frame update
    void Start()
    {
        Array[0] = Armature.transform.GetChild(0).gameObject;
    }

    // Update is called once per frame
    void LateUpdate()
    {
        //LoweArmL.transform.position += new Vector3(0.0005f, 0, 0);
        Array[0].transform.position += new Vector3(0.0005f, 0, 0);
    }
}
