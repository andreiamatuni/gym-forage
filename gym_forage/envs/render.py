from gym.envs.classic_control import rendering


red = (1.0, 0., 0.)
black = (0., 0., 0.)
green = (0., 1., 0.)

color_map = {
                1: green,
                0: black,
            -1000: red
            }

def render(viewer, view, c_width):
    # row 1
    l, r, t, b = 0.0, c_width, 3*c_width, 2*c_width
    c0 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c0.set_color(*color_map[view[0,0]])
    viewer.add_geom(c0)

    l, r, t, b = c_width, 2*c_width, 3*c_width, 2*c_width
    c1 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c1.set_color(*color_map[view[0,1]])
    viewer.add_geom(c1)

    l, r, t, b = 2*c_width, 3*c_width, 3*c_width, 2*c_width
    c2 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c2.set_color(*color_map[view[0,2]])
    viewer.add_geom(c2)

    # row 2
    l, r, t, b = 0.0, c_width, 2*c_width, 1*c_width
    c3 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c3.set_color(*color_map[view[1,0]])
    viewer.add_geom(c3)

    l, r, t, b = c_width, 2*c_width, 2*c_width, 1*c_width
    c4 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c4.set_color(*color_map[view[1,1]])
    viewer.add_geom(c4)

    l, r, t, b = 2*c_width, 3*c_width, 2*c_width, 1*c_width
    c5 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c5.set_color(*color_map[view[1,2]])
    viewer.add_geom(c5)

    # row 3
    l, r, t, b = 0.0, c_width, c_width, 0.0
    c6 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c6.set_color(*color_map[view[2,0]])
    viewer.add_geom(c6)

    l, r, t, b = c_width, 2*c_width, c_width, 0.0
    c7 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c7.set_color(*color_map[view[2,1]])
    viewer.add_geom(c7)

    l, r, t, b = 2*c_width, 3*c_width, c_width, 0.0
    c8 = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
    c8.set_color(*color_map[view[2,2]])
    viewer.add_geom(c8)
