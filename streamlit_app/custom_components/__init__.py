import os
import streamlit.components.v1 as components

# Set _RELEASE to True when you're ready to deploy the component
_RELEASE = False

if not _RELEASE:
    # In development mode, load the component from the React dev server
    _component_func = components.declare_component(
        "my_component", url="http://localhost:3000"
    )
else:
    # In production mode, load the component from the build folder
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)


def my_component(data: dict = None, key: str = None):
    """
    Streamlit custom component.

    Parameters
    ----------
    data : dict, optional
        Data to pass to the component.
    key : str, optional
        Unique key for the component.

    Returns
    -------
    Any
        Value returned by the component.
    """
    return _component_func(data=data, key=key)
