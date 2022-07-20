"""Downloadable datasets of 3D Celestial Bodies.

Examples
--------
>>> from pyvista import examples
>>> mesh = examples.planets.load_moon()
>>> mesh.plot()

"""
import numpy as np

import pyvista
from pyvista import examples


def load_sun(*args, **kwargs):
    """Load a sun source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_sun())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    surface = examples.download_sun_jpg()
    sphere.textures["atmosphere"] = surface
    return sphere


def load_moon(*args, **kwargs):
    """Load a moon source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_moon())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    surface = examples.download_moon_jpg()
    sphere.textures["surface"] = surface
    return sphere


def load_mercury(*args, **kwargs):
    """Load a mercury source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_mercury())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    surface = examples.download_mercury_jpg()
    sphere.textures["surface"] = surface
    return sphere


def load_venus(*args, **kwargs):
    """Load a venus source.

    Returns
    -------
    pyvista.PolyData
        Venus dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_venus())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    surface = examples.download_venus_jpg(atmosphere=False)
    sphere.textures["surface"] = surface
    atmosphere = examples.download_venus_jpg()
    sphere.textures["atmosphere"] = atmosphere
    return sphere


def load_mars(*args, **kwargs):
    """Load a mars source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_mars())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    surface = examples.planets.download_mars_jpg()
    sphere.textures["surface"] = surface
    return sphere


def load_jupiter(*args, **kwargs):
    """Load a jupiter source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_jupiter())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    atmosphere = examples.download_jupiter_jpg()
    sphere.textures["atmosphere"] = atmosphere
    return sphere


def load_saturn(*args, **kwargs):
    """Load a saturn source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_saturn())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    atmosphere = examples.download_saturn_jpg()
    sphere.textures["atmosphere"] = atmosphere
    return sphere


def load_saturn_ring_alpha(*args, **kwargs):
    """Load a saturn_ring_alpha source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_saturn_ring_alpha())
    >>> pl.show()

    """
    disc = pyvista.Disc(*args, **kwargs)
    disc.active_t_coords = np.zeros((disc.points.shape[0], 2))
    radius = np.sqrt(disc.points[:, 0] ** 2 + disc.points[:, 1] ** 2)
    disc.active_t_coords[:, 0] = radius / np.max(radius)
    disc.active_t_coords[:, 1] = 0.0
    atmosphere = examples.download_saturn_ring_alpha_png()
    disc.textures["atmosphere"] = atmosphere
    return disc


def load_uranus(*args, **kwargs):
    """Load a uranus source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_uranus())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    atmosphere = examples.download_uranus_jpg()
    sphere.textures["atmosphere"] = atmosphere
    return sphere


def load_neptune(*args, **kwargs):
    """Load a neptune source.

    Returns
    -------
    pyvista.PolyData
        Sun dataset with texture.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> pl = pyvista.Plotter()
    >>> pl.add_background_image(examples.download_stars_jpg())
    >>> _ = pl.add_mesh(examples.planets.load_neptune())
    >>> pl.show()

    """
    sphere = pyvista.Sphere(*args, **kwargs)
    sphere.texture_map_to_sphere(inplace=True)
    atmosphere = examples.download_neptune_jpg()
    sphere.textures["atmosphere"] = atmosphere
    return sphere


def download_sun_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'sun.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_sun_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('sun.jpg', texture=True, load=load)


def download_moon_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'moon.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_moon_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('moon.jpg', texture=True, load=load)


def download_mercury_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'mercury.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_mercury_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('mercury.jpg', texture=True, load=load)


def download_venus_jpg(atmosphere=True, load=True):  # pragma: no cover
    """Download and return the path of ``'venus.jpg'``.

    Parameters
    ----------
    atmosphere : bool, optional
        Load the atmosphere texture when ``True``.

    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_venus_jpg()
    >>> surface.plot(cpos="xy")

    """
    if atmosphere:
        return _download_and_read('venus_atmosphere.jpg', texture=True, load=load)
    else:
        return _download_and_read('venus_surface.jpg', texture=True, load=load)


def download_mars_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'mars.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_mars_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('mars.jpg', texture=True, load=load)


def download_jupiter_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'jupiter.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_jupiter_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('jupiter.jpg', texture=True, load=load)


def download_saturn_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'saturn.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_saturn_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('saturn.jpg', texture=True, load=load)


def download_saturn_ring_alpha_png(load=True):  # pragma: no cover
    """Download and return the path of ``'saturn_ring_alpha.png'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_saturn_ring_alpha_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('saturn_ring_alpha.png', texture=True, load=load)


def download_uranus_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'uranus.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_uranus_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('uranus.jpg', texture=True, load=load)


def download_neptune_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'neptune.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista
    >>> surface = examples.download_neptune_jpg()
    >>> surface.plot(cpos="xy")

    """
    return _download_and_read('neptune.jpg', texture=True, load=load)


def download_stars_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'stars.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista as pv
    >>> pl = pv.Plotter()
    >>> dataset = examples.download_stars_jpg()
    >>> pl.add_background_image(dataset)
    >>> pl.show()

    See :func:`download_mars_jpg` for another example using this dataset.

    """
    return _download_and_read('stars.jpg', load=load)


def download_milkyway_jpg(load=True):  # pragma: no cover
    """Download and return the path of ``'milkyway.jpg'``.

    Parameters
    ----------
    load : bool, optional
        Read the file. Default ``True``, when ``False``, return the path to the
        file.

    Returns
    -------
    str
        Filename of the JPEG.

    Examples
    --------
    >>> from pyvista import examples
    >>> import pyvista as pv
    >>> pl = pv.Plotter()
    >>> dataset = examples.download_milkyway_jpg()
    >>> pl.add_background_image(dataset)
    >>> pl.show()

    """
    return _download_and_read('milkyway.jpg', load=load)
