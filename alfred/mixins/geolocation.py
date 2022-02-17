from django.db.models.expressions import RawSQL


class AnnotateGeolocationMixin:
    def distance(self, lat, lon):
        # TODO: Utilizar a função nativa do MySQL que retorna a distância esférica entre
        # dois pontos. Desta forma evitamos vários hints no db.
        # https://dev.mysql.com/doc/refman/5.7/en/spatial-convenience-functions.html#function_st-distance-sphere
        # https://gitlab.com/maistodos/PortaldoParceiro/-/issues/347
        # return self.queryset.annotate(
        #     distance_km=RawSQL(
        #         "select ST_Distance_Sphere(point(longitude, latitude), "
        #         "point(%s, %s)) / 1000",
        #         [lon, lat],
        #     )
        # ).order_by("distance_km")

        # TODO: O código a seguir é um workaround enquanto não utilizamos a função
        # nativa do MySQL. A distância abaixo aproxima-se razoavelmente da distância
        # exata entre os dois pontos em linha reta.

        return (
            self.annotate(
                distance_km=RawSQL(
                    "SQRT( "
                    "POWER( (latitude - %s), 2) + "
                    "POWER( (longitude - %s), 2 ) ) * 100",
                    [lat, lon],
                )
            )
            .filter(distance_km__isnull=False)
            .order_by("distance_km")
        )
