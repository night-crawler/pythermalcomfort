# -*- coding: utf-8 -*-
"""
This code defines a dictionary called ALL_OUT_PARAMS that contains information about various output parameters
related to human body properties, heat exchange, and environmental conditions.

It also includes a function called show_outparam_docs() that generates a formatted string with the documentation
of the output parameters.

The show_outparam_docs() function uses text wrapping to create a readable documentation string
for both regular output parameters and extra output parameters.

It sorts the parameters alphabetically by key and formats each line with the parameter's name, meaning, and unit.
The resulting documentation string can be displayed or printed for user reference.
"""
import textwrap

ALL_OUT_PARAMS = {
    "age": {"ex_output": True, "meaning": "age", "suffix": None, "unit": "years"},
    "bf_ava_foot": {
        "ex_output": True,
        "meaning": "AVA blood flow rate of one foot",
        "suffix": None,
        "unit": "L/h",
    },
    "bf_ava_hand": {
        "ex_output": True,
        "meaning": "AVA blood flow rate of one hand",
        "suffix": None,
        "unit": "L/h",
    },
    "bf_core": {
        "ex_output": True,
        "meaning": "core blood flow rate (each body part)",
        "suffix": "Body name",
        "unit": "L/h",
    },
    "bf_fat": {
        "ex_output": True,
        "meaning": "fat blood flow rate (each body part)",
        "suffix": "Body name",
        "unit": "L/h",
    },
    "bf_muscle": {
        "ex_output": True,
        "meaning": "muscle blood flow rate (each body part)",
        "suffix": "Body name",
        "unit": "L/h",
    },
    "bf_skin": {
        "ex_output": True,
        "meaning": "skin blood flow rate (each body part)",
        "suffix": "Body name",
        "unit": "L/h",
    },
    "bsa": {
        "ex_output": True,
        "meaning": "body surface area (each body part)",
        "suffix": "Body name",
        "unit": "m2",
    },
    "cardiac_output": {
        "ex_output": False,
        "meaning": "cardiac output (the sum of the whole blood flow)",
        "suffix": None,
        "unit": "L/h",
    },
    "cycle_time": {
        "ex_output": False,
        "meaning": "the counts of executing one cycle calculation",
        "suffix": None,
        "unit": "-",
    },
    "e_max": {
        "ex_output": True,
        "meaning": "maximum evaporative heat loss from the skin (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "e_skin": {
        "ex_output": True,
        "meaning": "evaporative heat loss from the skin (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "e_sweat": {
        "ex_output": True,
        "meaning": "evaporative heat loss from the skin by only sweating (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "fat": {"ex_output": True, "meaning": "body fat rate", "suffix": None, "unit": "%"},
    "height": {"ex_output": True, "meaning": "body height", "suffix": None, "unit": "m"},
    "clo": {
        "ex_output": True,
        "meaning": "clothing insulation (each body part)",
        "suffix": "Body name",
        "unit": "clo",
    },
    "q_skin_latent": {
        "ex_output": True,
        "meaning": "latent heat loss from the skin (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_bmr_core": {
        "ex_output": True,
        "meaning": "core heat production by basal metabolism (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "met_base_fat": {
        "ex_output": True,
        "meaning": "fat heat production by basal metabolism (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_bmr_muscle": {
        "ex_output": True,
        "meaning": "muscle heat production by basal metabolism (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_bmr_skin": {
        "ex_output": True,
        "meaning": "skin heat production by basal metabolism (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_total": {
        "ex_output": False,
        "meaning": "total heat production of the whole body",
        "suffix": None,
        "unit": "W",
    },
    "Q_nst": {
        "ex_output": True,
        "meaning": "core heat production by non-shivering thermogenesis (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "simulation_time": {
        "ex_output": False,
        "meaning": "simulation times",
        "suffix": None,
        "unit": "sec",
    },
    "Q_shiv": {
        "ex_output": True,
        "meaning": "core or muscle heat production by shivering thermogenesis (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_work": {
        "ex_output": True,
        "meaning": "core or muscle heat production by work (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "name": {
        "ex_output": True,
        "meaning": "name of the model",
        "suffix": None,
        "unit": "-",
    },
    "par": {
        "ex_output": True,
        "meaning": "physical activity ratio",
        "suffix": None,
        "unit": "-",
    },
    "Q_core": {
        "ex_output": True,
        "meaning": "core total heat production (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_fat": {
        "ex_output": True,
        "meaning": "fat total heat production (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_muscle": {
        "ex_output": True,
        "meaning": "muscle total heat production (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "Q_skin": {
        "ex_output": True,
        "meaning": "skin total heat production (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "q_res": {
        "ex_output": False,
        "meaning": "heat loss by respiration",
        "suffix": None,
        "unit": "W",
    },
    "q_res_latent": {
        "ex_output": True,
        "meaning": "latent heat loss by respiration (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "q_res_sensible": {
        "ex_output": True,
        "meaning": "sensible heat loss by respiration (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "rh": {
        "ex_output": True,
        "meaning": "relative humidity (each body part)",
        "suffix": "Body name",
        "unit": "%",
    },
    "Ret": {
        "ex_output": True,
        "meaning": "total clothing evaporative heat resistance (each body part)",
        "suffix": "Body name",
        "unit": "m2.kPa/W",
    },
    "Rt": {
        "ex_output": True,
        "meaning": "total clothing heat resistance (each body part)",
        "suffix": "Body name",
        "unit": "m2.K/W",
    },
    "q_skin_sensible": {
        "ex_output": True,
        "meaning": "sensible heat loss from the skin (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "t_core_set": {
        "ex_output": True,
        "meaning": "skin set point temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_skin_set": {
        "ex_output": True,
        "meaning": "core set point temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "sex": {
        "ex_output": True,
        "meaning": "sex",
        "suffix": None,
        "unit": "-",
    },
    "q_skin": {
        "ex_output": False,
        "meaning": "total heat loss from the skin (each body part)",
        "suffix": "Body name",
        "unit": "W",
    },
    "tdb": {
        "ex_output": True,
        "meaning": "dry bulb air temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_artery": {
        "ex_output": True,
        "meaning": "arterial temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_cb": {
        "ex_output": True,
        "meaning": "central blood temperature",
        "suffix": None,
        "unit": "oC",
    },
    "t_core": {
        "ex_output": False,
        "meaning": "core temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_fat": {
        "ex_output": True,
        "meaning": "fat temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_muscle": {
        "ex_output": True,
        "meaning": "muscle temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "to": {
        "ex_output": True,
        "meaning": "operative temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "tr": {
        "ex_output": True,
        "meaning": "mean radiant temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_skin": {
        "ex_output": False,
        "meaning": "skin temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_skin_mean": {
        "ex_output": False,
        "meaning": "mean skin temperature",
        "suffix": None,
        "unit": "oC",
    },
    "t_superficial_vein": {
        "ex_output": True,
        "meaning": "superficial vein temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "t_vein": {
        "ex_output": True,
        "meaning": "vein temperature (each body part)",
        "suffix": "Body name",
        "unit": "oC",
    },
    "v": {
        "ex_output": True,
        "meaning": "air velocity (each body part)",
        "suffix": "Body name",
        "unit": "m/s",
    },
    "weight": {
        "ex_output": True,
        "meaning": "body weight",
        "suffix": None,
        "unit": "kg",
    },
    "w": {
        "ex_output": False,
        "meaning": "skin wettedness (each body part)",
        "suffix": "Body name",
        "unit": "-",
    },
    "w_mean": {
        "ex_output": False,
        "meaning": "mean skin wettedness",
        "suffix": None,
        "unit": "-",
    },
    "weight_loss_by_evap_and_res": {
        "ex_output": False,
        "meaning": "weight loss by the evaporation and respiration of the whole body",
        "suffix": None,
        "unit": "g/sec",
    },
    "dt": {
        "ex_output": False,
        "meaning": "time step",
        "suffix": None,
        "unit": "sec",
    },
    "pythermalcomfort_version": {
        "ex_output": False,
        "meaning": "version of pythermalcomfort",
        "suffix": None,
        "unit": "-",
    },
}


def show_outparam_docs():
    """
    Show the documentation of the output parameters.

    Returns
    -------
    docstirng : str
        Text of the documentation of the output parameters
    """

    outparams = textwrap.dedent(
        """
        Output parameters
        -------
        """
    )

    exoutparams = textwrap.dedent(
        """
        Extra output parameters
        -------
        """
    )

    sortkeys = list(ALL_OUT_PARAMS.keys())
    sortkeys.sort()
    for key in sortkeys:
        value = ALL_OUT_PARAMS[key]

        line = "{}: {} [{}]".format(key.ljust(8), value["meaning"], value["unit"])

        if value["ex_output"]:
            exoutparams += line + "\n"
        else:
            outparams += line + "\n"

    docs = outparams + "\n" + exoutparams
    docs = textwrap.indent(docs.strip(), "    ")

    return docs

if __name__ == "__main__":
    print(show_outparam_docs())
